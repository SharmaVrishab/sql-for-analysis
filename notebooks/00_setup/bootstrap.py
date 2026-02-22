"""Notebook bootstrap helper for importing local src package."""

from pathlib import Path
import sys


def ensure_src_on_path() -> Path:
    """Add repository src/ directory to sys.path and return its path."""
    root = Path(__file__).resolve().parents[2]
    src_dir = root / "src"
    src_str = str(src_dir)
    if src_str not in sys.path:
        sys.path.insert(0, src_str)
    return src_dir


if __name__ == "__main__":
    print(ensure_src_on_path())
