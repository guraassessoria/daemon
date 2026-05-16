from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import fitz
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

from common import DATA_DIR, INDEX_DIR, ROOT, TEXT_DIR, read_json, write_json


SOURCES_PATH = INDEX_DIR / "sources.json"
QUALITY_PATH = INDEX_DIR / "text-quality.json"
DUPLICATES_PATH = INDEX_DIR / "duplicates.json"
REPORT_PATH = INDEX_DIR / "ocr-report.json"
LOCAL_TESSDATA = DATA_DIR / "work" / "tessdata"
COMMON_TESSERACT_PATHS = [
    Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
    Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
]
COMMON_PT_WORDS = {
    "a", "ao", "aos", "as", "com", "como", "da", "das", "de", "do", "dos",
    "e", "em", "entre", "mais", "na", "nas", "no", "nos", "o", "os", "ou",
    "para", "por", "que", "se", "sua", "suas", "um", "uma", "seu", "seus",
    "personagem", "personagens", "daemon", "sistema", "regra", "regras",
    "pontos", "teste", "jogador", "mestre", "magia", "combate",
}


def find_tesseract() -> Path:
    found = shutil.which("tesseract")
    if found:
        return Path(found)
    for candidate in COMMON_TESSERACT_PATHS:
        if candidate.exists():
            return candidate
    raise SystemExit("Tesseract executable not found.")


def local_languages() -> set[str]:
    if not LOCAL_TESSDATA.exists():
        return set()
    return {path.stem for path in LOCAL_TESSDATA.glob("*.traineddata")}


def choose_language(requested: str | None) -> str:
    if requested:
        return requested
    langs = local_languages()
    if "por" in langs and "eng" in langs:
        return "por+eng"
    if "por" in langs:
        return "por"
    if "eng" in langs:
        return "eng"
    return "eng"


def duplicate_ids() -> set[str]:
    payload = read_json(DUPLICATES_PATH, {"duplicates": []})
    return {row["duplicate"] for row in payload.get("duplicates", [])}


def quality_target_ids() -> list[str]:
    payload = read_json(QUALITY_PATH, {"sources": []})
    duplicates = duplicate_ids()
    return [
        row["id"]
        for row in payload.get("sources", [])
        if row.get("status") == "needs_ocr" and row.get("id") not in duplicates
    ]


def source_by_id() -> dict[str, dict]:
    payload = read_json(SOURCES_PATH, {"sources": []})
    return {source["id"]: source for source in payload.get("sources", [])}


def ocr_page(
    tesseract: Path,
    image_path: Path,
    language: str,
    tessdata_dir: Path | None,
    timeout: int,
    psm: int | None,
) -> str:
    command = [str(tesseract), str(image_path), "stdout", "-l", language]
    if tessdata_dir and tessdata_dir.exists():
        command.extend(["--tessdata-dir", str(tessdata_dir)])
    if psm is not None:
        command.extend(["--psm", str(psm)])

    env = os.environ.copy()
    env["OMP_THREAD_LIMIT"] = env.get("OMP_THREAD_LIMIT", "1")
    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )
    if completed.returncode != 0:
        stderr = completed.stderr.strip()
        raise RuntimeError(stderr or f"Tesseract failed with code {completed.returncode}")
    return completed.stdout.strip()


def score_text(text: str) -> float:
    stripped = text.strip()
    if not stripped:
        return -1000

    words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", stripped)
    alpha_words = [word for word in words if any(char.isalpha() for char in word)]
    useful_words = [word for word in alpha_words if len(word) >= 2]
    common_hits = sum(1 for word in useful_words if word.casefold() in COMMON_PT_WORDS)
    symbol_count = sum(1 for char in stripped if not char.isalnum() and not char.isspace() and char not in ".,;:!?()[]/%+-ºª")
    replacement_count = stripped.count("\ufffd")
    single_letter_ratio = (
        sum(1 for word in alpha_words if len(word) == 1) / max(1, len(alpha_words))
    )
    very_long_words = sum(1 for word in alpha_words if len(word) > 28)

    return (
        len(useful_words) * 8
        + common_hits * 20
        + len(stripped) * 0.08
        - symbol_count * 3
        - replacement_count * 80
        - single_letter_ratio * 140
        - very_long_words * 15
    )


def ocr_page_adaptive(
    tesseract: Path,
    image_path: Path,
    language: str,
    tessdata_dir: Path | None,
    timeout: int,
    psm_candidates: list[int | None],
) -> tuple[str, str]:
    candidates: list[tuple[float, str, str]] = []
    for psm in psm_candidates:
        text = ocr_page(tesseract, image_path, language, tessdata_dir, timeout, psm)
        label = "default" if psm is None else f"psm{psm}"
        candidates.append((score_text(text), label, text))
    _, label, text = max(candidates, key=lambda item: item[0])
    return text, label


def render_page(page: fitz.Page, image_path: Path, dpi: int) -> None:
    scale = dpi / 72
    pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    pixmap.save(image_path)


def preprocess_image(image_path: Path, mode: str) -> None:
    if mode == "none":
        return

    image = Image.open(image_path).convert("L")
    if mode == "gray":
        image = ImageOps.autocontrast(image)
    elif mode == "contrast-sharp":
        image = ImageOps.autocontrast(image)
        image = ImageEnhance.Contrast(image).enhance(1.7)
        image = image.filter(ImageFilter.SHARPEN)
    elif mode == "threshold180":
        image = ImageOps.autocontrast(image)
        image = image.point(lambda pixel: 255 if pixel > 180 else 0)
    elif mode == "threshold200":
        image = ImageOps.autocontrast(image)
        image = image.point(lambda pixel: 255 if pixel > 200 else 0)
    elif mode == "median-threshold":
        image = ImageOps.autocontrast(image)
        image = image.filter(ImageFilter.MedianFilter(3))
        image = image.point(lambda pixel: 255 if pixel > 185 else 0)
    else:
        raise ValueError(f"Unknown preprocess mode: {mode}")

    image.save(image_path)


def run_ocr_for_source(
    source: dict,
    tesseract: Path,
    language: str,
    dpi: int,
    timeout: int,
    force: bool,
    psm: int | None,
    adaptive: bool,
    adaptive_psm: list[int | None],
    preprocess: str,
) -> dict:
    source_id = source["id"]
    output_path = TEXT_DIR / f"{source_id}.txt"
    if output_path.exists() and not force:
        existing = output_path.read_text(encoding="utf-8", errors="ignore").strip()
        if len(existing) > 1000:
            return {"id": source_id, "status": "skipped_existing", "chars": len(existing)}

    pdf_path = ROOT / source["path"]
    started = time.monotonic()
    page_results: list[str] = []
    errors: list[str] = []
    mode_counts: dict[str, int] = {}
    tessdata_dir = LOCAL_TESSDATA if LOCAL_TESSDATA.exists() else None

    with fitz.open(pdf_path) as document, tempfile.TemporaryDirectory(prefix=f"ocr-{source_id}-") as tmp:
        tmp_dir = Path(tmp)
        page_count = document.page_count
        for page_index in range(page_count):
            page_number = page_index + 1
            image_path = tmp_dir / f"page-{page_number:04d}.png"
            try:
                render_page(document.load_page(page_index), image_path, dpi)
                preprocess_image(image_path, preprocess)
                if adaptive:
                    text, mode = ocr_page_adaptive(
                        tesseract, image_path, language, tessdata_dir, timeout, adaptive_psm
                    )
                else:
                    text = ocr_page(tesseract, image_path, language, tessdata_dir, timeout, psm)
                    mode = "default" if psm is None else f"psm{psm}"
                mode_counts[mode] = mode_counts.get(mode, 0) + 1
            except Exception as exc:  # noqa: BLE001 - record and keep the book moving.
                text = ""
                mode = "error"
                mode_counts[mode] = mode_counts.get(mode, 0) + 1
                errors.append(f"page {page_number}: {exc}")
            page_results.append(f"--- page {page_number} ---\n{text}".rstrip())
            print(f"{source_id}: page {page_number}/{page_count}", flush=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = "\n\n".join(page_results).rstrip() + "\n"
    output_path.write_text(output, encoding="utf-8")
    return {
        "id": source_id,
        "status": "done" if not errors else "done_with_errors",
        "pages": len(page_results),
        "chars": len(output.strip()),
        "errors": errors,
        "modes": mode_counts,
        "seconds": round(time.monotonic() - started, 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*", help="Source ids to OCR. Defaults to canonical needs_ocr sources.")
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--timeout", type=int, default=120, help="Seconds per page.")
    parser.add_argument("--lang", default=None)
    parser.add_argument("--psm", type=int, default=None, help="Optional Tesseract page segmentation mode.")
    parser.add_argument(
        "--preprocess",
        default="none",
        choices=["none", "gray", "contrast-sharp", "threshold180", "threshold200", "median-threshold"],
        help="Image cleanup applied before OCR.",
    )
    parser.add_argument("--adaptive", action="store_true", help="Try multiple page segmentation modes and keep the best page result.")
    parser.add_argument(
        "--adaptive-psm",
        default="default,4,11",
        help="Comma-separated PSM candidates for --adaptive. Use 'default' for Tesseract default.",
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    tesseract = find_tesseract()
    language = choose_language(args.lang)
    adaptive_psm = [
        None if value.strip().casefold() == "default" else int(value.strip())
        for value in args.adaptive_psm.split(",")
        if value.strip()
    ]
    sources = source_by_id()
    ids = args.ids or quality_target_ids()

    report = {
        "version": 1,
        "tesseract": str(tesseract),
        "language": language,
        "dpi": args.dpi,
        "psm": args.psm,
        "adaptive": args.adaptive,
        "adaptivePsm": ["default" if value is None else value for value in adaptive_psm],
        "preprocess": args.preprocess,
        "sources": [],
    }

    for source_id in ids:
        source = sources.get(source_id)
        if not source:
            report["sources"].append({"id": source_id, "status": "missing_source"})
            continue
        if source.get("extension") != ".pdf":
            report["sources"].append({"id": source_id, "status": "not_pdf"})
            continue
        print(f"Starting OCR: {source_id}", flush=True)
        result = run_ocr_for_source(
            source=source,
            tesseract=tesseract,
            language=language,
            dpi=args.dpi,
            timeout=args.timeout,
            force=args.force,
            psm=args.psm,
            adaptive=args.adaptive,
            adaptive_psm=adaptive_psm,
            preprocess=args.preprocess,
        )
        report["sources"].append(result)
        write_json(REPORT_PATH, report)

    write_json(REPORT_PATH, report)
    print(f"OCR report written to {REPORT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
