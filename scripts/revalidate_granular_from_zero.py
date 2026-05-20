from __future__ import annotations

import argparse
import subprocess
import sys

from common import INDEX_DIR, ROOT, write_json
from granular_validation import LOCK_FILE_BY_AREA


ORDERED_STEPS = [
    ("aprimoramentos", ["scripts/extract_granular_aprimoramentos.py"], ["scripts/certify_aprimoramentos.py"]),
    ("kits", ["scripts/extract_granular_kits.py"], ["scripts/certify_kits.py"]),
    # Classes remains between kits and races to avoid legacy class/profession records leaking into later categories.
    ("classes", ["scripts/extract_granular_classes.py"], ["scripts/certify_classes.py"]),
    ("racas_linhagens", ["scripts/extract_granular_racas.py"], ["scripts/certify_racas.py"]),
    ("regras_base", ["scripts/extract_granular_regras_base.py"], ["scripts/certify_regras_base.py"]),
    ("poderes_magias", ["scripts/extract_granular_poderes_magias.py"], ["scripts/certify_poderes_magias.py"]),
    ("rituais", ["scripts/extract_granular_rituais.py"], ["scripts/certify_rituais.py"]),
]


def reset_locks() -> None:
    for area, path_name in LOCK_FILE_BY_AREA.items():
        write_json(
            INDEX_DIR / path_name,
            {
                "version": 1,
                "area": area,
                "policy": {"reset_for_full_granular_revalidation": True},
                "certifiedCount": 0,
                "records": [],
            },
        )


def run(label: str, command: list[str], dry_run: bool = False) -> None:
    final = [sys.executable, *command]
    print(f"[granular-zero] {label}: {' '.join(final)}")
    if not dry_run:
        subprocess.run(final, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Revalidates the granular catalog from zero in lock order.")
    parser.add_argument("--dry-run", action="store_true", help="Show the ordered commands without executing them.")
    parser.add_argument("--no-build", action="store_true", help="Do not rebuild area catalog and GitHub Pages data.")
    args = parser.parse_args()

    print("[granular-zero] Resetting certification locks.")
    if not args.dry_run:
        reset_locks()

    for area, extract_command, certify_command in ORDERED_STEPS:
        run(f"extract {area}", extract_command, args.dry_run)
        run(f"certify {area}", certify_command, args.dry_run)

    if not args.no_build:
        run("build area catalog", ["scripts/build_area_catalog.py"], args.dry_run)
        run("publish github pages data", ["scripts/build_github_pages_site.py"], args.dry_run)


if __name__ == "__main__":
    main()
