from __future__ import annotations

import shutil
from pathlib import Path

from common import DATA_DIR, ROOT


DOCS_DIR = ROOT / "docs"
PAGES_DATA_DIR = DOCS_DIR / "assets" / "data"


def copy_json_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def main() -> None:
    PAGES_DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / ".nojekyll").touch()

    copy_json_file(DATA_DIR / "index" / "area-summary.json", PAGES_DATA_DIR / "area-summary.json")

    areas_target = PAGES_DATA_DIR / "areas"
    if areas_target.exists():
        shutil.rmtree(areas_target)
    areas_target.mkdir(parents=True, exist_ok=True)

    for source in sorted((DATA_DIR / "areas").glob("*.json")):
        copy_json_file(source, areas_target / source.name)

    print(f"GitHub Pages data copied to {PAGES_DATA_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
