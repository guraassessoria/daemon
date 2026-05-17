const state = {
  summary: null,
  area: null,
  areaData: null,
  items: [],
  selectedId: null,
  query: "",
  type: "all",
  category: "all",
  typeByArea: readTypePrefs(),
  searchTimer: null,
};

const nodes = {
  metrics: document.querySelector("#metrics"),
  areaList: document.querySelector("#areaList"),
  areaOverview: document.querySelector("#areaOverview"),
  results: document.querySelector("#results"),
  resultsTitle: document.querySelector("#resultsTitle"),
  resultsCount: document.querySelector("#resultsCount"),
  detailPane: document.querySelector("#detailPane"),
  searchInput: document.querySelector("#searchInput"),
  typeFilter: document.querySelector("#typeFilter"),
  categoryFilter: document.querySelector("#categoryFilter"),
  refreshButton: document.querySelector("#refreshButton"),
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

const typeFilterMap = {
  entities: "entity",
  sourceParts: "sourcePart",
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

function readTypePrefs() {
  try {
    return JSON.parse(sessionStorage.getItem("daemonTools.typeByArea") ?? "{}");
  } catch {
    return {};
  }
}

function writeTypePrefs() {
  sessionStorage.setItem("daemonTools.typeByArea", JSON.stringify(state.typeByArea));
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

function overviewTile(label, value) {
  const tile = document.createElement("div");
  tile.className = "overview-tile";
  const number = document.createElement("strong");
  number.textContent = value;
  const text = document.createElement("span");
  text.textContent = label;
  tile.append(number, text);
  return tile;
}

function renderOverview() {
  const area = state.areaData;
  nodes.areaOverview.replaceChildren(
    overviewTile("entidades", area.entityCount),
    overviewTile("partes dos livros", area.sourcePartCount),
    overviewTile("fontes", area.readySourceCount),
  );
  nodes.resultsTitle.textContent = area.name;
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

function renderCategoryFilter() {
  const categories = [...new Set(state.items.map((item) => item.category).filter(Boolean))].sort();
  const current = state.category;
  const options = [new Option("Todas", "all"), ...categories.map((category) => new Option(category, category))];
  nodes.categoryFilter.replaceChildren(...options);
  nodes.categoryFilter.value = categories.includes(current) ? current : "all";
  state.category = nodes.categoryFilter.value;
}

function itemSummary(item) {
  if (item.summary) return item.summary;
  if (Array.isArray(item.entries) && item.entries.length) return item.entries.join(" ");
  return "Sem resumo nesta passada.";
}

function itemPage(item) {
  if (item.page) return item.page;
  if (Array.isArray(item.pages) && item.pages.length) return item.pages.join(", ");
  return "-";
}

function itemKind(item) {
  if (item.classKind) return `${subtypeLabels[item.subtype] ?? "Classe"}: ${item.classKind}`;
  return subtypeLabels[item.subtype] ?? typeLabels[item.itemType] ?? item.itemType;
}

function filteredItems() {
  const query = normalize(state.query);
  return state.items.filter((item) => {
    if (state.type !== "all" && item.itemType !== typeFilterMap[state.type]) return false;
    if (state.category !== "all" && item.category !== state.category) return false;
    if (!query) return true;
    return item.normalizedSearchable.includes(query);
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
    empty.textContent = "Nenhum item encontrado com os filtros atuais.";
    state.selectedId = null;
    nodes.results.replaceChildren(empty);
    renderDetail();
    return;
  }

  if (!items.some((item) => item.id === state.selectedId)) {
    state.selectedId = items[0].id;
  }

  nodes.results.replaceChildren(...items.map(renderItemRow));
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
  if (item.costText) addMeta(meta, "Custo", item.costText);
  if (Array.isArray(item.costs) && item.costs.length) addMeta(meta, "Custos", item.costs.join(", "));
  if (item.classKind) addMeta(meta, "Classe", item.classKind);

  const body = document.createElement("section");
  body.className = "detail-body";
  const entries = Array.isArray(item.entries) && item.entries.length ? item.entries : [item.summary || ""];
  entries.filter(Boolean).forEach((entry) => {
    const block = document.createElement("p");
    block.textContent = entry;
    body.append(block);
  });

  const tags = document.createElement("div");
  tags.className = "detail-tags";
  renderTags(tags, [
    ...(item.certifiedAs ? [`certificado: ${item.certifiedAs}`] : []),
    ...(item.lockedArea ? [`trava: ${item.lockedArea}`] : []),
    ...(item.tags ?? []),
  ]);

  nodes.detailPane.replaceChildren(header, meta, body, tags);
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
  const text = String(value ?? "").replace(/\s+/g, " ").trim();
  if (text.length <= maxLength) return text || "-";
  return `${text.slice(0, maxLength - 1).trim()}…`;
}

async function selectArea(areaId, options = {}) {
  state.area = areaId;
  state.areaData = await fetchJson(`assets/data/areas/${areaId}.json`);
  state.items = buildItems(state.areaData);
  state.type = state.typeByArea[areaId] ?? (state.areaData.entityCount > 0 ? "entities" : "all");
  if (state.type === "entities" && state.areaData.entityCount === 0) state.type = "all";
  if (state.type === "sourceParts" && state.areaData.sourcePartCount === 0) state.type = "all";
  state.selectedId = options.itemId ?? null;
  nodes.typeFilter.value = state.type;
  renderAreaList();
  renderOverview();
  renderCategoryFilter();
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

nodes.typeFilter.addEventListener("change", (event) => {
  state.type = event.target.value;
  state.typeByArea[state.area] = state.type;
  writeTypePrefs();
  renderResults();
  renderDetail();
});

nodes.categoryFilter.addEventListener("change", (event) => {
  state.category = event.target.value;
  renderResults();
  renderDetail();
});

nodes.refreshButton.addEventListener("click", () => {
  load().catch(showError);
});

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

load().catch(showError);
