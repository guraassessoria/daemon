const state = {
  summary: null,
  area: null,
  areaData: null,
  items: [],
  query: "",
  type: "all",
  category: "all",
};

const nodes = {
  metrics: document.querySelector("#metrics"),
  areaList: document.querySelector("#areaList"),
  areaOverview: document.querySelector("#areaOverview"),
  results: document.querySelector("#results"),
  resultsTitle: document.querySelector("#resultsTitle"),
  resultsCount: document.querySelector("#resultsCount"),
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

function metric(label, value) {
  const element = document.createElement("div");
  element.className = "metric";
  element.innerHTML = `<strong>${value}</strong><span>${label}</span>`;
  return element;
}

function renderMetrics() {
  nodes.metrics.replaceChildren(
    metric("fontes prontas", state.summary.readySourceCount),
    metric("areas", state.summary.areaCount),
    metric("partes", state.summary.sourcePartCount),
    metric("entidades", state.summary.entityCount),
  );
}

function renderAreaList() {
  const buttons = state.summary.areas.map((area) => {
    const fragment = nodes.areaButtonTemplate.content.cloneNode(true);
    const button = fragment.querySelector("button");
    button.dataset.area = area.id;
    button.classList.toggle("active", state.area === area.id);
    fragment.querySelector(".area-name").textContent = area.name;
    fragment.querySelector(".area-count").textContent = `${area.entityCount} ent. / ${area.sourcePartCount} blocos`;
    button.addEventListener("click", () => selectArea(area.id));
    return fragment;
  });
  nodes.areaList.replaceChildren(...buttons);
}

function overviewTile(label, value) {
  const tile = document.createElement("div");
  tile.className = "overview-tile";
  tile.innerHTML = `<strong>${value}</strong><span>${label}</span>`;
  return tile;
}

function renderOverview() {
  const area = state.areaData;
  nodes.areaOverview.replaceChildren(
    overviewTile("entidades curadas", area.entityCount),
    overviewTile("partes dos livros", area.sourcePartCount),
    overviewTile("fontes prontas", area.readySourceCount),
  );
  nodes.resultsTitle.textContent = area.name;
}

function buildItems(areaData) {
  const entities = areaData.entities.map((item) => ({
    ...item,
    itemType: "entity",
    searchable: [
      item.name,
      item.sourceTitle,
      item.category,
      ...(item.entries ?? []),
      ...(item.tags ?? []),
    ].join(" "),
  }));
  const sourceParts = areaData.sourceParts.map((item) => ({
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
  return [...entities, ...sourceParts];
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

function renderTags(container, tags) {
  const visibleTags = (tags ?? []).slice(0, 5);
  container.replaceChildren(
    ...visibleTags.map((tag) => {
      const element = document.createElement("span");
      element.className = "tag";
      element.textContent = tag;
      return element;
    }),
  );
}

function itemKind(item) {
  if (item.classKind) return `${subtypeLabels[item.subtype] ?? "Classe"}: ${item.classKind}`;
  return subtypeLabels[item.subtype] ?? typeLabels[item.itemType] ?? item.itemType;
}

function renderItem(item) {
  const fragment = nodes.itemTemplate.content.cloneNode(true);
  fragment.querySelector(".item-kind").textContent = itemKind(item);
  fragment.querySelector(".item-source").textContent = item.sourceTitle || item.source || "-";
  fragment.querySelector("h3").textContent = item.name || item.id;
  fragment.querySelector(".summary").textContent = itemSummary(item);
  fragment.querySelector(".item-category").textContent = item.category || "-";
  fragment.querySelector(".item-page").textContent = itemPage(item);
  fragment.querySelector(".item-confidence").textContent = item.confidence ?? "-";
  renderTags(fragment.querySelector(".tags"), [
    ...(item.costText ? [item.costText] : []),
    ...(item.costs ?? []),
    ...(item.tags ?? []),
  ]);
  return fragment;
}

function filteredItems() {
  const query = normalize(state.query);
  return state.items.filter((item) => {
    if (state.type !== "all" && item.itemType !== typeFilterMap[state.type]) return false;
    if (state.category !== "all" && item.category !== state.category) return false;
    if (!query) return true;
    return normalize(item.searchable).includes(query);
  });
}

function renderResults() {
  const items = filteredItems();
  nodes.resultsCount.textContent = `${items.length} item(ns)`;

  if (!items.length) {
    const empty = document.createElement("div");
    empty.className = "empty";
    empty.textContent = "Nenhum item encontrado com os filtros atuais.";
    nodes.results.replaceChildren(empty);
    return;
  }

  nodes.results.replaceChildren(...items.map(renderItem));
}

async function selectArea(areaId) {
  state.area = areaId;
  state.areaData = await fetchJson(`assets/data/areas/${areaId}.json`);
  state.items = buildItems(state.areaData);
  state.type = state.areaData.entityCount > 0 ? "entities" : "all";
  nodes.typeFilter.value = state.type;
  renderAreaList();
  renderOverview();
  renderCategoryFilter();
  renderResults();
}

async function load() {
  nodes.results.replaceChildren();
  state.summary = await fetchJson("assets/data/area-summary.json");
  state.area = state.summary.areas[0]?.id;
  renderMetrics();
  renderAreaList();
  await selectArea(state.area);
}

nodes.searchInput.addEventListener("input", (event) => {
  state.query = event.target.value;
  renderResults();
});

nodes.typeFilter.addEventListener("change", (event) => {
  state.type = event.target.value;
  renderResults();
});

nodes.categoryFilter.addEventListener("change", (event) => {
  state.category = event.target.value;
  renderResults();
});

nodes.refreshButton.addEventListener("click", () => {
  load().catch(showError);
});

function showError(error) {
  const empty = document.createElement("div");
  empty.className = "empty";
  empty.textContent = error.message;
  nodes.results.replaceChildren(empty);
}

load().catch(showError);
