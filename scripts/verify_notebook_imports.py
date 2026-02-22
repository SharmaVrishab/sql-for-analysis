"""Validation script that enforces centralized db import in notebooks."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS_DIR = ROOT / "notebooks"

LEGACY_IMPORT = "from db_connection import get_connection"
EXPECTED_IMPORT = "from sql_for_analysis.db.connection import get_connection"
EXPECTED_BOOTSTRAP = "from pathlib import Path"
EXPECTED_BOOTSTRAP_HELPER = "from bootstrap import ensure_src_on_path"


def notebook_contains_text(path: Path, text: str) -> bool:
    payload = json.loads(path.read_text(encoding="utf-8"))
    for cell in payload.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if text in source:
            return True
    return False


def main() -> int:
    notebooks = sorted(NOTEBOOKS_DIR.rglob("*.ipynb"))
    failed = False

    for nb in notebooks:
        if notebook_contains_text(nb, LEGACY_IMPORT):
            print(f"FAIL legacy import found: {nb}")
            failed = True
        if not notebook_contains_text(nb, EXPECTED_IMPORT):
            print(f"FAIL expected shared import missing: {nb}")
            failed = True
        if not notebook_contains_text(nb, EXPECTED_BOOTSTRAP):
            print(f"FAIL bootstrap block missing: {nb}")
            failed = True
        if not notebook_contains_text(nb, EXPECTED_BOOTSTRAP_HELPER):
            print(f"FAIL bootstrap helper import missing: {nb}")
            failed = True

    if failed:
        return 1

    print(f"PASS validated {len(notebooks)} notebooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
