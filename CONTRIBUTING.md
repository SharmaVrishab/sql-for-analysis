# Contributing

## Setup

1. Create a virtual environment.
2. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

3. Run validation before opening a PR:

```bash
PYTHONPATH=src python3 -m pytest -q
python3 scripts/verify_notebook_imports.py
```

## Standards

- Keep notebook imports aligned with the shared module:
  - `from sql_for_analysis.db.connection import get_connection`
- Do not add notebook-local connection helpers.
- Keep committed data lightweight and non-sensitive.
- Write clear commit messages and include context in PR descriptions.
