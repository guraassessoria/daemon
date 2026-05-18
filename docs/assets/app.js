const state = {
  summary: null,
  area: null,
  areaData: null,
  items: [],
  selectedId: null,
  query: "",
  theme: readThemePref(),
  searchTimer: null,
};

const nodes = {
  metrics: document.querySelector("#metrics"),
  areaList: document.querySelector("#areaList"),
  results: document.querySelector("#results"),
  resultsTitle: document.querySelector("#resultsTitle"),
  resultsCount: document.querySelector("#resultsCount"),
  detailPane: document.querySelector("#detailPane"),
  searchInput: document.querySelector("#searchInput"),
  refreshButton: document.querySelector("#refreshButton"),
  themeToggle: document.querySelector("#themeToggle"),
  areaButtonTemplate: document.querySelector("#areaButtonTemplate"),
  itemTemplate: document.querySelector("#itemTemplate"),
};

const typeLabels = {
  entity: "Entidade",
  sourcePart: "Parte",
};

const subtypeLabels = {
  aprimoramento: "Aprimoramento",
  class: "Classe",
  kit: "Kit",
  linhagem: "Linhagem",
  magia: "Magia",
  poder: "Poder",
  raca: "Raça",
  ritual: "Ritual",
};

async function fetchJson(path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) {
    throw new Error(`Nao foi possivel carregar ${path}`);
  }
  return response.json();
}

function normalize(value) {
  return String(value ?? "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase();
}

function preferredSystemTheme() {
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function readThemePref() {
  return localStorage.getItem("daemonTools.theme") || preferredSystemTheme();
}

function applyTheme(theme) {
  state.theme = theme === "dark" ? "dark" : "light";
  document.documentElement.dataset.theme = state.theme;
  nodes.themeToggle?.setAttribute("aria-pressed", state.theme === "dark" ? "true" : "false");
  nodes.themeToggle?.setAttribute("title", state.theme === "dark" ? "Usar tema claro" : "Usar tema escuro");
}

function toggleTheme() {
  const nextTheme = state.theme === "dark" ? "light" : "dark";
  localStorage.setItem("daemonTools.theme", nextTheme);
  applyTheme(nextTheme);
}

function setText(element, value) {
  element.textContent = value ?? "-";
}

function metric(label, value) {
  const element = document.createElement("div");
  element.className = "metric";
  const number = document.createElement("strong");
  number.textContent = value;
  const text = document.createElement("span");
  text.textContent = label;
  element.append(number, text);
  return element;
}

function renderMetrics() {
  nodes.metrics.replaceChildren(
    metric("fontes prontas", state.summary.readySourceCount),
    metric("areas", state.summary.areaCount),
    metric("itens", state.summary.entityCount),
    metric("blocos", state.summary.sourcePartCount),
  );
}

function renderAreaList() {
  const buttons = state.summary.areas.map((area) => {
    const fragment = nodes.areaButtonTemplate.content.cloneNode(true);
    const button = fragment.querySelector("button");
    button.dataset.area = area.id;
    button.classList.toggle("active", state.area === area.id);
    if (state.area === area.id) button.setAttribute("aria-current", "page");
    setText(fragment.querySelector(".area-name"), area.name);
    setText(fragment.querySelector(".area-count"), `${area.entityCount}/${area.sourcePartCount}`);
    button.addEventListener("click", () => selectArea(area.id));
    return fragment;
  });
  nodes.areaList.replaceChildren(...buttons);
}

function renderOverview() {
  nodes.resultsTitle.textContent = state.areaData.name;
}

function buildItems(areaData) {
  const entities = (areaData.entities ?? []).map((item) => ({
    ...item,
    itemType: "entity",
    searchable: [
      item.name,
      item.sourceTitle,
      item.category,
      item.certifiedAs,
      item.subgroup,
      item.subgroupLabel,
      item.costText,
      ...(item.costs ?? []),
      ...(item.entries ?? []),
      ...(item.tags ?? []),
    ].join(" "),
  }));
  const sourceParts = (areaData.sourceParts ?? []).map((item) => ({
    ...item,
    itemType: "sourcePart",
    searchable: [
      item.name,
      item.sourceTitle,
      item.category,
      item.summary,
      ...(item.tags ?? []),
    ].join(" "),
  }));
  return [...entities, ...sourceParts].map((item) => ({
    ...item,
    normalizedSearchable: normalize(item.searchable),
  }));
}

function itemSummary(item) {
  if (item.summary) return item.summary;
  if (Array.isArray(item.entries) && item.entries.length) return item.entries.join(" ");
  return "Sem resumo nesta passada.";
}

function formatEntryText(raw) {
  let text = String(raw ?? "")
    .replace(/\r\n?/g, "\n")
    .replace(/\u00ad/g, "")
    .replace(/(\p{L})-\n(?=\p{L})/gu, "$1")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n[ \t]+/g, "\n")
    .replace(/\n{3,}/g, "\n\n");

  text = text
    .split(/\n{2,}/)
    .map((paragraph) =>
      paragraph
        .split("\n")
        .map((line) => line.trim())
        .filter(Boolean)
        .join(" "),
    )
    .join("\n\n");

  return text.replace(/\n?\s*\d{1,3}\s*$/g, "").trim();
}

function splitEntryBlocks(raw) {
  const text = formatEntryText(raw);
  if (!text) return [];
  const markerRe = /(?:^|\s)((?:[-\u2010-\u2015\u2212]\s*)?\d+\s+PONTOS?\s*:|\bCUSTO\s*:)/gi;
  const markerIndexes = [];
  let match;
  while ((match = markerRe.exec(text)) !== null) {
    markerIndexes.push(match.index + match[0].indexOf(match[1]));
  }
  if (!markerIndexes.length || markerIndexes[0] !== 0) markerIndexes.unshift(0);

  return markerIndexes
    .map((start, index) => text.slice(start, markerIndexes[index + 1]).trim())
    .filter(Boolean);
}

function isCostBlock(text) {
  return /^(?:[-\u2010-\u2015\u2212]\s*)?\d+\s+PONTOS?\s*:|^CUSTO\s*:/i.test(text);
}

function isNegativeCostBlock(text) {
  return /^[-\u2010-\u2015\u2212]\s*\d+\s+PONTOS?\s*:/i.test(text);
}

function itemPage(item) {
  if (item.page) return item.page;
  if (Array.isArray(item.pages) && item.pages.length) return item.pages.join(", ");
  return "-";
}

function itemKind(item) {
  if (item.subtype === "aprimoramento" && item.subgroupLabel) {
    return item.subgroupLabel.replace(/^Aprimoramentos\s+/i, "Aprimoramento ");
  }
  if (item.classKind) return `${subtypeLabels[item.subtype] ?? "Classe"}: ${item.classKind}`;
  return subtypeLabels[item.subtype] ?? typeLabels[item.itemType] ?? item.itemType;
}

function filteredItems() {
  const query = normalize(state.query);
  return state.items
    .filter((item) => !query || item.normalizedSearchable.includes(query))
    .sort(compareItemsByName);
}

function compareItemsByName(left, right) {
  return (left.name || left.id || "").localeCompare(right.name || right.id || "", "pt-BR", {
    sensitivity: "base",
    numeric: true,
  }) || (left.sourceTitle || left.source || "").localeCompare(right.sourceTitle || right.source || "", "pt-BR", {
    sensitivity: "base",
    numeric: true,
  });
}

function selectItem(itemId, options = {}) {
  state.selectedId = itemId;
  updateActiveRows();
  renderDetail();
  if (!options.skipHash) {
    updateHash();
  }
}

function updateActiveRows() {
  nodes.results.querySelectorAll(".item-row").forEach((row) => {
    const isActive = row.dataset.itemId === state.selectedId;
    row.classList.toggle("active", isActive);
    row.setAttribute("aria-selected", isActive ? "true" : "false");
  });
}

function renderItemRow(item) {
  const fragment = nodes.itemTemplate.content.cloneNode(true);
  const button = fragment.querySelector(".item-row");
  button.dataset.itemId = item.id;
  button.classList.toggle("active", item.id === state.selectedId);
  button.setAttribute("aria-selected", item.id === state.selectedId ? "true" : "false");
  setText(fragment.querySelector(".item-title"), item.name || item.id);
  setText(fragment.querySelector(".item-preview"), compactText(itemSummary(item), 140));
  setText(fragment.querySelector(".item-kind"), itemKind(item));
  setText(fragment.querySelector(".item-source"), item.sourceTitle || item.source || "-");
  button.addEventListener("click", () => selectItem(item.id));
  return fragment;
}

function renderResults() {
  const items = filteredItems();
  nodes.resultsCount.textContent = `${items.length} item(ns)`;

  if (!items.length) {
    const empty = document.createElement("div");
    empty.className = "empty";
    empty.textContent = "Nenhum item encontrado com a busca atual.";
    state.selectedId = null;
    nodes.results.replaceChildren(empty);
    renderDetail();
    return;
  }

  if (!items.some((item) => item.id === state.selectedId)) {
    state.selectedId = items[0].id;
  }

  if (state.area === "aprimoramentos") {
    renderAprimoramentoGroups(items);
    return;
  }

  nodes.results.replaceChildren(...items.map(renderItemRow));
}

function renderAprimoramentoGroups(items) {
  const groups = [
    ["aprimoramentos_positivos", "Aprimoramentos Positivos"],
    ["aprimoramentos_negativos", "Aprimoramentos Negativos"],
  ];
  const grouped = new Map(groups.map(([id]) => [id, []]));
  items.forEach((item) => {
    const groupId = item.subgroup ?? "aprimoramentos_positivos";
    if (!grouped.has(groupId)) grouped.set(groupId, []);
    grouped.get(groupId).push(item);
  });

  const elements = groups
    .map(([id, label]) => renderResultGroup(id, label, grouped.get(id) ?? []))
    .filter(Boolean);
  nodes.results.replaceChildren(...elements);
}

function renderResultGroup(id, label, items) {
  if (!items.length) return null;

  const details = document.createElement("details");
  details.className = "result-group";
  details.dataset.group = id;
  details.open = true;

  const summary = document.createElement("summary");
  summary.className = "result-group-summary";

  const title = document.createElement("span");
  title.textContent = label;

  const count = document.createElement("span");
  count.className = "result-group-count";
  count.textContent = `${items.length}`;

  const list = document.createElement("div");
  list.className = "result-group-items";
  list.append(...items.map(renderItemRow));

  summary.append(title, count);
  details.append(summary, list);
  return details;
}

function renderDetail(explicitItem) {
  const item = explicitItem ?? state.items.find((candidate) => candidate.id === state.selectedId);
  if (!item) {
    const empty = document.createElement("div");
    empty.className = "empty detail-empty";
    empty.textContent = "Selecione um item na lista.";
    nodes.detailPane.replaceChildren(empty);
    return;
  }

  const header = document.createElement("header");
  header.className = "detail-header";

  const kind = document.createElement("span");
  kind.className = "pill";
  kind.textContent = itemKind(item);

  const title = document.createElement("h2");
  title.textContent = item.name || item.id;

  const source = document.createElement("p");
  source.className = "detail-source";
  source.textContent = item.sourceTitle || item.source || "Fonte não identificada";

  header.append(kind, title, source);

  const meta = document.createElement("dl");
  meta.className = "detail-meta";
  addMeta(meta, "Categoria", item.category || "-");
  addMeta(meta, "Pagina", itemPage(item));
  addMeta(meta, "Confianca", item.confidence ?? "-");
  addMeta(meta, "Tipo", typeLabels[item.itemType] ?? item.itemType);
  if (item.classKind) addMeta(meta, "Classe", item.classKind);

  const facts = renderDetailFacts(item);
  const body = document.createElement("section");
  body.className = "detail-body";
  const entries = Array.isArray(item.entries) && item.entries.length ? item.entries : [item.summary || ""];
  renderEntryBlocks(body, entries);

  const tags = document.createElement("div");
  tags.className = "detail-tags";
  renderTags(tags, [
    ...(item.certifiedAs ? [`certificado: ${item.certifiedAs}`] : []),
    ...(item.lockedArea ? [`trava: ${item.lockedArea}`] : []),
    ...(item.tags ?? []),
  ]);

  nodes.detailPane.replaceChildren(header, meta, facts, body, tags);
}

function addMeta(container, label, value) {
  const wrapper = document.createElement("div");
  const term = document.createElement("dt");
  const description = document.createElement("dd");
  term.textContent = label;
  description.textContent = value;
  wrapper.append(term, description);
  container.append(wrapper);
}

function renderDetailFacts(item) {
  const facts = document.createElement("section");
  facts.className = "detail-facts";
  const rows = [
    ["Custo", item.costText],
    ["Custos detectados", Array.isArray(item.costs) ? item.costs.join(", ") : ""],
    ["Subgrupo", item.subgroupLabel],
    ["Requisitos", item.requirements],
    ["Pericias", item.skillsText],
    ["Atributos", item.attributesText],
    ["Vantagens", item.advantagesText],
    ["Desvantagens", item.disadvantagesText],
    ["Contexto de classe", item.classContext],
    ["Contexto racial", item.raceContext],
    ["Contexto magico", item.powerMagicContext],
    ["Contexto ritual", item.ritualContext],
  ].filter(([, value]) => value !== undefined && value !== null && String(value).trim());

  if (!rows.length) {
    facts.hidden = true;
    return facts;
  }

  const list = document.createElement("dl");
  rows.forEach(([label, value]) => addMeta(list, label, formatEntryText(value)));
  facts.append(list);
  return facts;
}

function renderEntryBlocks(container, entries) {
  entries.filter(Boolean).forEach((entry) => {
    const blocks = splitEntryBlocks(entry);
    let costList = null;
    const shouldListCosts = blocks.filter((block) => isCostBlock(block) && !isNegativeCostBlock(block)).length > 1;

    blocks.forEach((block) => {
      if (isCostBlock(block) && !isNegativeCostBlock(block) && shouldListCosts) {
        if (!costList) {
          costList = document.createElement("ul");
          costList.className = "cost-tiers";
          container.append(costList);
        }
        const item = document.createElement("li");
        item.textContent = block;
        costList.append(item);
        return;
      }

      costList = null;
      block.split(/\n{2,}/).filter(Boolean).forEach((paragraph) => {
        const element = document.createElement("p");
        element.textContent = paragraph;
        container.append(element);
      });
    });
  });
}

function renderTags(container, tags) {
  const visibleTags = [...new Set(tags.filter(Boolean))].slice(0, 16);
  container.replaceChildren(
    ...visibleTags.map((tag) => {
      const element = document.createElement("span");
      element.className = "tag";
      element.textContent = tag;
      return element;
    }),
  );
}

function compactText(value, maxLength) {
  const text = formatEntryText(value).replace(/\s+/g, " ").trim();
  if (text.length <= maxLength) return text || "-";
  return `${text.slice(0, maxLength - 1).trim()}…`;
}

async function selectArea(areaId, options = {}) {
  state.area = areaId;
  state.areaData = await fetchJson(`assets/data/areas/${areaId}.json`);
  state.items = buildItems(state.areaData);
  state.selectedId = options.itemId ?? null;
  renderAreaList();
  renderOverview();
  renderResults();
  renderDetail();
  if (!options.skipHash) {
    updateHash();
  }
}

function updateHash() {
  if (!state.area) return;
  const nextHash = state.selectedId ? `#${state.area}/${state.selectedId}` : `#${state.area}`;
  if (window.location.hash !== nextHash) {
    window.history.replaceState(null, "", nextHash);
  }
}

function hashState() {
  const [areaId, itemId] = window.location.hash.replace(/^#/, "").split("/");
  return { areaId, itemId };
}

async function load() {
  state.summary = await fetchJson("assets/data/area-summary.json");
  const hash = hashState();
  const initialArea = state.summary.areas.some((area) => area.id === hash.areaId)
    ? hash.areaId
    : state.summary.areas[0]?.id;

  renderMetrics();
  renderAreaList();
  await selectArea(initialArea, { itemId: hash.itemId, skipHash: Boolean(hash.areaId) });
}

nodes.searchInput.addEventListener("input", (event) => {
  window.clearTimeout(state.searchTimer);
  state.searchTimer = window.setTimeout(() => {
    state.query = event.target.value;
    renderResults();
    renderDetail();
  }, 180);
});

nodes.refreshButton.addEventListener("click", () => {
  load().catch(showError);
});

nodes.themeToggle?.addEventListener("click", toggleTheme);

window.addEventListener("hashchange", () => {
  const hash = hashState();
  if (!hash.areaId || hash.areaId === state.area) {
    if (hash.itemId && state.items.some((item) => item.id === hash.itemId)) {
      selectItem(hash.itemId, { skipHash: true });
    }
    return;
  }
  selectArea(hash.areaId, { itemId: hash.itemId, skipHash: true }).catch(showError);
});

function showError(error) {
  const empty = document.createElement("div");
  empty.className = "empty";
  empty.textContent = error.message;
  nodes.results.replaceChildren(empty);
  nodes.detailPane.replaceChildren(empty.cloneNode(true));
}

applyTheme(state.theme);
load().catch(showError);
