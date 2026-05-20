const STORAGE = {
  theme: "daemonTools.theme",
  sourceMode: "daemonTools.sourceMode",
  qualityMode: "daemonTools.qualityMode",
  selectedSources: "daemonTools.selectedSources",
  selectedFamilies: "daemonTools.selectedFamilies",
  selectedKinds: "daemonTools.selectedKinds",
  showEditorialNotes: "daemonTools.showEditorialNotes",
};

const state = {
  summary: null,
  area: null,
  areaData: null,
  areaCache: {},
  items: [],
  selectedId: null,
  query: "",
  theme: readThemePref(),
  sourceMode: localStorage.getItem(STORAGE.sourceMode) || "all",
  qualityMode: readQualityMode(),
  selectedSources: readSet(STORAGE.selectedSources),
  selectedFamilies: readSet(STORAGE.selectedFamilies),
  selectedKinds: readSet(STORAGE.selectedKinds),
  showEditorialNotes: localStorage.getItem(STORAGE.showEditorialNotes) === "true",
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
  adminToggle: document.querySelector("#adminToggle"),
  adminClose: document.querySelector("#adminClose"),
  adminPanel: document.querySelector("#adminPanel"),
  sourceMode: document.querySelector("#sourceMode"),
  qualityMode: document.querySelector("#qualityMode"),
  sourceFilter: document.querySelector("#sourceFilter"),
  familyFilter: document.querySelector("#familyFilter"),
  kindFilter: document.querySelector("#kindFilter"),
  notesToggle: document.querySelector("#notesToggle"),
  clearFilters: document.querySelector("#clearFilters"),
  activeFilters: document.querySelector("#activeFilters"),
  areaButtonTemplate: document.querySelector("#areaButtonTemplate"),
  itemTemplate: document.querySelector("#itemTemplate"),
};

const typeLabels = {
  entity: "Registro",
  sourcePart: "Trecho de livro",
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

const contentKindLabels = {
  source_catalog: "Ficha de fonte/livro",
  rule_mechanic: "Regra ou mecânica",
  character_option: "Opção de personagem",
  power_spell: "Poder, magia ou ritual",
  combat_maneuver: "Combate ou manobra",
  item_equipment: "Item, equipamento ou material",
  creature_npc: "Criatura, inimigo ou NPC",
  lore_world: "História, mundo ou cenário",
  organization_faction: "Organização, facção ou culto",
  adventure_scene: "Aventura, cena ou campanha",
  table_reference: "Tabela ou referência",
  raw_chapter_block: "Capítulo/página bruto",
  front_matter: "Créditos, índice ou metadado",
  ocr_noise: "OCR/lixo de extração",
  uncertain_fragment: "Fragmento incerto",
};

const qualityLabels = {
  empty_display_text: "sem texto exibível",
  too_short_possible_cut: "possível corte",
  ends_with_connector_possible_cut: "termina incompleto",
  does_not_end_like_complete_sentence: "fim possivelmente incompleto",
  too_long_possible_merged_blocks: "blocos possivelmente colados",
  encoding_or_ocr_artifact: "artefato de OCR/codificação",
  hyphenated_word_split: "palavra hifenizada",
  page_number_inside_text: "número de página misturado",
  trailing_section_footer_or_page_number: "rodapé misturado",
  unbalanced_parentheses: "parênteses desbalanceados",
  unbalanced_brackets: "colchetes desbalanceados",
  repeated_fragment_possible_duplication: "fragmento repetido",
  aprimoramento_without_cost_marker: "aprimoramento sem custo",
  many_cost_markers_possible_merged_aprimoramentos: "custos demais no bloco",
  starts_mid_sentence_possible_left_cut: "começa no meio da frase",
  lowercase_sentence_after_section_possible_leak: "possível trecho colado",
  invalid_title_or_ocr_header: "título inválido/OCR",
  critical_ocr_gibberish: "OCR crítico",
  symbol_noise_ocr: "ruído de símbolos",
  front_matter_or_index_block: "front matter/sumário",
  generic_chapter_or_page_block: "capítulo genérico",
  source_part_without_specific_subject: "trecho sem assunto específico",
  ocr_corrupted_title_or_body: "texto corrompido",
  raw_source_part_requires_review: "trecho bruto para revisão",
  manual_quarantine: "quarentena manual",
  manual_review: "revisão manual",
};

const duplicateHintLabels = {
  repeated_fragment_possible_duplication:
    "Há trecho repetido neste registro; compare com a fonte antes de manter como entrada independente.",
  many_cost_markers_possible_merged_aprimoramentos:
    "Há vários marcadores de custo no mesmo bloco; pode haver aprimoramentos diferentes misturados.",
  too_long_possible_merged_blocks: "O bloco está longo para uma única entrada; verifique se mais de um item foi unido.",
  front_matter_or_generic_duplicate:
    "O conteúdo parece front matter ou bloco genérico repetido em outra fonte.",
  near_duplicate_same_information: "Pode repetir a mesma informação de outro registro com pequenas variações de texto.",
};

const semanticSectionLabels = [
  "Alcance",
  "Aprimoramentos",
  "Atributos",
  "Beneficio",
  "Beneficios",
  "Caminhos Preferidos",
  "Consequencia",
  "Consequencias",
  "Custo",
  "Custos",
  "Dano",
  "Descricao",
  "Descricao",
  "Desvantagens",
  "Duracao",
  "Duracao",
  "Efeito",
  "Especial",
  "Funcionamento",
  "Habilidades",
  "Limitacoes",
  "Limitacoes",
  "Observacao",
  "Observacao",
  "Pericias",
  "Pericias",
  "Pericias Obrigatorias",
  "Pericias Obrigatorias",
  "Pericias Sugeridas",
  "Pericias Sugeridas",
  "Poderes",
  "Pontos de Fe",
  "Pontos de Fe",
  "Pontos de Magia",
  "Pontos Heroicos",
  "Pontos Heroicos",
  "Regras",
  "Requisito",
  "Requisitos",
  "Restricoes",
  "Restricoes",
  "Sistema",
  "Tempo de Conjuracao",
  "Tempo de Conjuracao",
  "Teste",
  "Testes",
  "Vantagens",
];

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

function readSet(key) {
  try {
    const value = JSON.parse(localStorage.getItem(key) || "[]");
    return new Set(Array.isArray(value) ? value : []);
  } catch {
    return new Set();
  }
}

function saveSet(key, value) {
  localStorage.setItem(key, JSON.stringify([...value]));
}

function readQualityMode() {
  const saved = localStorage.getItem(STORAGE.qualityMode) || "catalog";
  return ["catalog", "review", "quarantine"].includes(saved) ? saved : "catalog";
}

function preferredSystemTheme() {
  return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

function readThemePref() {
  return localStorage.getItem(STORAGE.theme) || preferredSystemTheme();
}

function applyTheme(theme) {
  state.theme = theme === "dark" ? "dark" : "light";
  document.documentElement.dataset.theme = state.theme;
  nodes.themeToggle?.setAttribute("aria-pressed", state.theme === "dark" ? "true" : "false");
  nodes.themeToggle?.setAttribute("title", state.theme === "dark" ? "Usar tema claro" : "Usar tema escuro");
}

function toggleTheme() {
  const nextTheme = state.theme === "dark" ? "light" : "dark";
  localStorage.setItem(STORAGE.theme, nextTheme);
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
      item.sourceKindLabel,
      item.sourceFamilyLabel,
      item.contentKindLabel,
      item.qualityStatus,
      item.costText,
      ...(item.costs ?? []),
      ...(item.entries ?? []),
      ...(item.entityRefs ?? []),
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
      item.sourceKindLabel,
      item.sourceFamilyLabel,
      item.contentKindLabel,
      item.qualityStatus,
      ...(item.entityRefs ?? []),
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

function shouldShowEditorialNotes() {
  return state.showEditorialNotes || state.qualityMode === "review" || state.qualityMode === "quarantine";
}

function semanticLabelSet() {
  return new Set(semanticSectionLabels.map((label) => normalize(label).replace(/\s+/g, " ").trim()));
}

function splitSemanticSections(raw) {
  const text = formatEntryText(raw);
  if (!text) return [];
  const labels = semanticLabelSet();
  const headingRe = /(^|[\s.;])([\p{L}][\p{L}\s]{1,34})\s*:/gu;
  const matches = [];
  let match;
  while ((match = headingRe.exec(text)) !== null) {
    const label = match[2].replace(/\s+/g, " ").trim();
    if (!labels.has(normalize(label).replace(/\s+/g, " ").trim())) continue;
    const markerStart = match.index + match[1].length;
    matches.push({
      start: markerStart,
      contentStart: headingRe.lastIndex,
      label: normalizeHeading(label),
    });
  }

  if (!matches.length) return [{ kind: "text", text }];
  const sections = [];
  if (matches[0].start > 0) {
    sections.push({ kind: "text", text: text.slice(0, matches[0].start).trim() });
  }
  matches.forEach((item, index) => {
    sections.push({
      kind: "section",
      label: item.label,
      text: text.slice(item.contentStart, matches[index + 1]?.start).trim(),
    });
  });
  return sections.filter((section) => section.text);
}

function normalizeHeading(value) {
  return String(value ?? "")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/\b\p{L}/gu, (letter) => letter.toLocaleUpperCase("pt-BR"));
}

function splitReadableParagraphs(value) {
  return formatEntryText(value)
    .split(/\n{2,}/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean);
}

function appendParagraphs(container, value) {
  splitReadableParagraphs(value).forEach((paragraph) => {
    const element = document.createElement("p");
    element.textContent = paragraph;
    container.append(element);
  });
}

function renderStructuredText(container, value) {
  const sections = splitSemanticSections(value);
  if (sections.length === 1 && sections[0].kind === "text") {
    appendParagraphs(container, sections[0].text);
    return;
  }

  sections.forEach((section) => {
    if (section.kind === "text") {
      appendParagraphs(container, section.text);
      return;
    }

    const wrapper = document.createElement("section");
    wrapper.className = "semantic-section";
    const title = document.createElement("h3");
    title.className = "semantic-heading";
    title.textContent = section.label;
    wrapper.append(title);
    appendParagraphs(wrapper, section.text);
    container.append(wrapper);
  });
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
    .filter(filterByQuality)
    .filter(filterBySourceMode)
    .filter(filterByFamily)
    .filter(filterByKind)
    .filter(filterBySource)
    .sort(compareItemsByName);
}

function filterByQuality(item) {
  const status = item.presentationStatus || "public";
  const severity = item.qualitySeverity || "ok";
  if (state.qualityMode === "quarantine") return status === "quarantine";
  if (state.qualityMode === "review") return status !== "quarantine" && severity !== "ok";
  return status !== "quarantine";
}

function filterBySourceMode(item) {
  if (state.sourceMode === "official") return Boolean(item.officialSource);
  if (state.sourceMode === "supplement") return item.officialSource === false;
  return true;
}

function filterByFamily(item) {
  return !state.selectedFamilies.size || state.selectedFamilies.has(item.sourceFamily);
}

function filterByKind(item) {
  const kind = item.contentKind || item.subtype || item.itemType;
  return !state.selectedKinds.size || state.selectedKinds.has(kind);
}

function filterBySource(item) {
  return !state.selectedSources.size || state.selectedSources.has(item.source);
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
  const warning = fragment.querySelector(".item-warning");
  const badge = qualityBadgeText(item);
  if (badge) {
    warning.hidden = false;
    warning.textContent = badge;
  }
  setText(fragment.querySelector(".item-source"), item.sourceTitle || item.source || "-");
  button.addEventListener("click", () => selectItem(item.id));
  return fragment;
}

function qualityBadgeText(item) {
  if (item.presentationStatus === "quarantine") return "quarentena";
  if (item.qualitySeverity === "critical") return "crítico";
  if (item.qualitySeverity === "warning" || (item.qualityFlags ?? []).length) return "revisar";
  return "";
}

function renderResults() {
  const items = filteredItems();
  nodes.resultsCount.textContent = `${items.length} item(ns)`;

  if (!items.length) {
    const empty = document.createElement("div");
    empty.className = "empty";
    empty.textContent = "Nenhum item encontrado com a busca ou filtros atuais.";
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
  addMeta(meta, "Fonte", item.sourceKindLabel || (item.officialSource ? "Livro oficial" : "Suplemento"));
  addMeta(meta, "Família", item.sourceFamilyLabel || "-");
  addMeta(meta, "Conteúdo", item.contentKindLabel || contentKindLabels[item.contentKind] || item.subtype || "-");
  if (item.classKind) addMeta(meta, "Classe", item.classKind);

  const qualityAlert = renderQualityAlert(item);
  const facts = renderDetailFacts(item);
  const body = document.createElement("section");
  body.className = "detail-body";
  const entries = Array.isArray(item.entries) && item.entries.length ? item.entries : [item.summary || ""];
  renderEntryBlocks(body, entries);
  renderTables(body, item.tables);
  const duplicateHints = renderDuplicateHints(item);
  const entityRefs = renderEntityRefs(item);

  const tags = document.createElement("div");
  tags.className = "detail-tags";
  renderTags(tags, [
    ...(item.certifiedAs ? [`certificado: ${item.certifiedAs}`] : []),
    ...(item.lockedArea ? [`trava: ${item.lockedArea}`] : []),
    ...(item.sourceKindLabel ? [item.sourceKindLabel] : []),
    ...(item.sourceFamilyLabel ? [item.sourceFamilyLabel] : []),
    ...(item.contentKindLabel ? [item.contentKindLabel] : []),
    ...(item.tags ?? []),
  ]);

  nodes.detailPane.replaceChildren(header, meta, qualityAlert, facts, body, duplicateHints, entityRefs, tags);
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

function renderQualityAlert(item) {
  const wrapper = document.createElement("section");
  const flags = item.qualityFlags ?? [];
  if (!flags.length || !shouldShowEditorialNotes()) {
    wrapper.hidden = true;
    return wrapper;
  }
  wrapper.className = "quality-alert";
  const title = document.createElement("strong");
  title.textContent = item.presentationStatus === "quarantine" ? "Quarentena editorial" : "Avisos editoriais";
  const list = document.createElement("ul");
  list.className = "quality-list";
  flags.slice(0, 12).forEach((flag) => {
    const entry = document.createElement("li");
    entry.textContent = qualityLabels[flag] || flag.replaceAll("_", " ");
    list.append(entry);
  });
  wrapper.append(title, list);
  return wrapper;
}

function renderDuplicateHints(item) {
  const wrapper = document.createElement("section");
  wrapper.className = "detail-note duplicate-hints";
  const hints = duplicateHints(item);
  if (!hints.length) {
    wrapper.hidden = true;
    return wrapper;
  }

  const title = document.createElement("h3");
  title.textContent = "Dicas de duplicidade";
  const list = document.createElement("ul");
  hints.slice(0, 6).forEach((hint) => {
    const entry = document.createElement("li");
    entry.textContent = hint;
    list.append(entry);
  });
  wrapper.append(title, list);
  return wrapper;
}

function duplicateHints(item) {
  const hints = [];
  const addHint = (value) => {
    const text = formatEntryText(value);
    if (text && !hints.includes(text)) hints.push(text);
  };

  (item.duplicateHints ?? []).forEach(addHint);
  (item.possibleDuplicateHints ?? []).forEach(addHint);
  (item.possibleDuplicates ?? []).forEach((duplicate) => {
    const label = duplicateLabel(duplicate);
    if (label) addHint(`Possível duplicidade com ${label}.`);
  });
  (item.duplicates ?? []).forEach((duplicate) => {
    const label = duplicateLabel(duplicate);
    if (label) addHint(`Conteúdo relacionado ou repetido em ${label}.`);
  });
  if (item.duplicateOf) addHint(`Este registro pode ser duplicata de ${duplicateLabel(item.duplicateOf)}.`);

  (item.qualityFlags ?? []).forEach((flag) => {
    if (duplicateHintLabels[flag]) addHint(duplicateHintLabels[flag]);
  });

  return hints;
}

function duplicateLabel(value) {
  if (!value) return "";
  if (typeof value === "string") return value;
  return value.name || value.title || value.id || value.sourceTitle || "";
}

function renderEntityRefs(item) {
  const wrapper = document.createElement("section");
  wrapper.className = "detail-note entity-refs";
  const refs = normalizedRefs(item.entityRefs);
  if (!refs.length) {
    wrapper.hidden = true;
    return wrapper;
  }

  const title = document.createElement("h3");
  title.textContent = "Referências";
  const list = document.createElement("div");
  list.className = "reference-list";

  refs.slice(0, 18).forEach((ref) => {
    const target = findReferenceTarget(ref.id);
    const element = document.createElement(target ? "button" : "span");
    element.className = `reference-chip${target ? "" : " unresolved"}`;
    element.textContent = target?.name || ref.label || ref.id;
    element.title = target ? "Abrir registro relacionado" : "Referência ainda não publicada nesta área";
    if (target) {
      element.type = "button";
      element.addEventListener("click", () => selectItem(target.id));
    }
    list.append(element);
  });

  wrapper.append(title, list);
  return wrapper;
}

function normalizedRefs(refs) {
  if (!Array.isArray(refs)) return [];
  return refs
    .map((ref) => {
      if (typeof ref === "string") return { id: ref, label: ref };
      return { id: ref.id || ref.slug || ref.ref || "", label: ref.name || ref.title || ref.label || ref.id };
    })
    .filter((ref) => ref.id);
}

function findReferenceTarget(refId) {
  const normalizedRef = normalize(refId);
  return state.items.find((item) => {
    const candidates = [item.id, item.slug, item.name].filter(Boolean).map(normalize);
    return candidates.includes(normalizedRef);
  });
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
      renderStructuredText(container, block);
    });
  });
}

function renderTables(container, tables) {
  if (!Array.isArray(tables) || !tables.length) return;
  tables.forEach((tableData, index) => {
    const wrapper = document.createElement("section");
    wrapper.className = "table-card";
    const title = document.createElement("h3");
    title.textContent = tableData.title || `Tabela ${index + 1}`;
    const scroll = document.createElement("div");
    scroll.className = "table-scroll";
    const table = document.createElement("table");
    table.className = "rules-table";
    const columns = Array.isArray(tableData.columns) ? tableData.columns : [];
    const rows = Array.isArray(tableData.rows) ? tableData.rows : [];
    if (columns.length) {
      const thead = document.createElement("thead");
      const tr = document.createElement("tr");
      columns.forEach((column) => {
        const th = document.createElement("th");
        th.textContent = column;
        tr.append(th);
      });
      thead.append(tr);
      table.append(thead);
    }
    const tbody = document.createElement("tbody");
    rows.forEach((row) => {
      const tr = document.createElement("tr");
      const values = Array.isArray(row) ? row : columns.map((column) => row?.[column] ?? "");
      values.forEach((value) => {
        const td = document.createElement("td");
        td.textContent = value ?? "";
        tr.append(td);
      });
      tbody.append(tr);
    });
    table.append(tbody);
    scroll.append(table);
    wrapper.append(title, scroll);
    container.append(wrapper);
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

function checkboxOptions(container, options, selected, emptyText) {
  container.replaceChildren();
  if (!options.length) {
    const empty = document.createElement("span");
    empty.className = "filter-empty";
    empty.textContent = emptyText;
    container.append(empty);
    return;
  }
  options.forEach((option) => {
    const label = document.createElement("label");
    label.className = "filter-check";
    const input = document.createElement("input");
    input.type = "checkbox";
    input.value = option.id;
    input.checked = selected.has(option.id);
    const text = document.createElement("span");
    text.textContent = `${option.label || option.title || option.id} (${option.count})`;
    label.append(input, text);
    container.append(label);
  });
}

function selectedOptions(container) {
  return new Set([...container.querySelectorAll("input:checked")].map((input) => input.value));
}

function pruneSelected(set, allowed) {
  const allowedIds = new Set(allowed.map((item) => item.id));
  for (const value of [...set]) {
    if (!allowedIds.has(value)) set.delete(value);
  }
}

function renderAdminFilters() {
  if (!state.areaData) return;
  const filters = state.areaData.filters || {};
  const families = filters.sourceFamilies || [];
  const sources = filters.sources || [];
  const kinds = (filters.subtypes || []).map((item) => ({
    ...item,
    label: contentKindLabels[item.id] || subtypeLabels[item.id] || item.id,
  }));
  pruneSelected(state.selectedFamilies, families);
  pruneSelected(state.selectedSources, sources);
  pruneSelected(state.selectedKinds, kinds);
  nodes.qualityMode.value = state.qualityMode;
  nodes.sourceMode.value = state.sourceMode;
  nodes.notesToggle.setAttribute("aria-pressed", state.showEditorialNotes ? "true" : "false");
  nodes.notesToggle.textContent = state.showEditorialNotes ? "Ocultar avisos" : "Mostrar avisos";
  checkboxOptions(nodes.familyFilter, families, state.selectedFamilies, "Nenhuma família disponível.");
  checkboxOptions(nodes.sourceFilter, sources, state.selectedSources, "Nenhuma fonte disponível.");
  checkboxOptions(nodes.kindFilter, kinds, state.selectedKinds, "Nenhum tipo disponível.");
  renderFilterSummary();
}

function renderFilterSummary() {
  const modeLabels = {
    catalog: "Catálogo normal",
    review: "Revisar",
    quarantine: "Quarentena",
  };
  const chips = [modeLabels[state.qualityMode] || state.qualityMode];
  if (state.sourceMode === "official") chips.push("Oficiais");
  if (state.sourceMode === "supplement") chips.push("Suplementos");
  if (state.selectedFamilies.size) chips.push(`${state.selectedFamilies.size} família(s)`);
  if (state.selectedSources.size) chips.push(`${state.selectedSources.size} fonte(s)`);
  if (state.selectedKinds.size) chips.push(`${state.selectedKinds.size} tipo(s)`);
  if (state.showEditorialNotes) chips.push("avisos visíveis");
  nodes.activeFilters.replaceChildren(
    ...chips.map((chip) => {
      const element = document.createElement("span");
      element.className = "filter-chip";
      element.textContent = chip;
      return element;
    }),
  );
}

function applyAdminFilters() {
  saveSet(STORAGE.selectedFamilies, state.selectedFamilies);
  saveSet(STORAGE.selectedSources, state.selectedSources);
  saveSet(STORAGE.selectedKinds, state.selectedKinds);
  localStorage.setItem(STORAGE.sourceMode, state.sourceMode);
  localStorage.setItem(STORAGE.qualityMode, state.qualityMode);
  localStorage.setItem(STORAGE.showEditorialNotes, state.showEditorialNotes ? "true" : "false");
  renderFilterSummary();
  renderResults();
  renderDetail();
}

function setAdminOpen(open) {
  nodes.adminPanel.hidden = !open;
  nodes.adminToggle.setAttribute("aria-expanded", open ? "true" : "false");
  if (open) {
    const firstFocusable = nodes.adminPanel.querySelector("select, input, button");
    firstFocusable?.focus();
  } else {
    nodes.adminToggle.focus();
  }
}

async function selectArea(areaId, options = {}) {
  state.area = areaId;
  if (!state.areaCache[areaId]) {
    state.areaCache[areaId] = await fetchJson(`assets/data/areas/${areaId}.json`);
  }
  state.areaData = state.areaCache[areaId];
  state.items = buildItems(state.areaData);
  state.selectedId = options.itemId ?? null;
  renderAreaList();
  renderOverview();
  renderAdminFilters();
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

nodes.adminToggle.addEventListener("click", () => {
  setAdminOpen(nodes.adminPanel.hidden);
});

nodes.adminClose.addEventListener("click", () => {
  setAdminOpen(false);
});

nodes.qualityMode.addEventListener("change", (event) => {
  state.qualityMode = event.target.value;
  applyAdminFilters();
});

nodes.sourceMode.addEventListener("change", (event) => {
  state.sourceMode = event.target.value;
  applyAdminFilters();
});

nodes.familyFilter.addEventListener("change", () => {
  state.selectedFamilies = selectedOptions(nodes.familyFilter);
  applyAdminFilters();
});

nodes.sourceFilter.addEventListener("change", () => {
  state.selectedSources = selectedOptions(nodes.sourceFilter);
  applyAdminFilters();
});

nodes.kindFilter.addEventListener("change", () => {
  state.selectedKinds = selectedOptions(nodes.kindFilter);
  applyAdminFilters();
});

nodes.notesToggle.addEventListener("click", () => {
  state.showEditorialNotes = !state.showEditorialNotes;
  renderAdminFilters();
  applyAdminFilters();
});

nodes.clearFilters.addEventListener("click", () => {
  state.sourceMode = "all";
  state.qualityMode = "catalog";
  state.selectedSources = new Set();
  state.selectedFamilies = new Set();
  state.selectedKinds = new Set();
  state.showEditorialNotes = false;
  renderAdminFilters();
  applyAdminFilters();
});

nodes.refreshButton.addEventListener("click", () => {
  state.areaCache = {};
  load().catch(showError);
});

nodes.themeToggle?.addEventListener("click", toggleTheme);

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !nodes.adminPanel.hidden) {
    setAdminOpen(false);
  }
});

nodes.results.addEventListener("keydown", (event) => {
  if (!["ArrowUp", "ArrowDown"].includes(event.key)) return;
  event.preventDefault();
  const rows = [...nodes.results.querySelectorAll(".item-row")];
  if (!rows.length) return;
  const currentIndex = rows.findIndex((row) => row.dataset.itemId === state.selectedId);
  const nextIndex =
    event.key === "ArrowDown"
      ? Math.min(currentIndex + 1, rows.length - 1)
      : Math.max(currentIndex - 1, 0);
  if (nextIndex !== currentIndex) {
    selectItem(rows[nextIndex].dataset.itemId);
    rows[nextIndex].focus();
  }
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

applyTheme(state.theme);
load().catch(showError);
