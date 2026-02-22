# SQL for Data Engineering Roadmap

[![CI Ready](https://img.shields.io/badge/CI-ready-brightgreen)](.github/workflows/ci.yml)

Hands-on **SQL roadmap for data engineering** using notebooks, practice problems, and production-style patterns.

This repository is optimized for:
- Structured SQL learning from fundamentals to advanced patterns.
- Recruiter-friendly portfolio visibility on GitHub.
- Reproducible notebook workflows with shared utilities.

## Why This Repo

If you are learning SQL for roles like **Data Engineer**, **Analytics Engineer**, or **BI Developer**, this roadmap focuses on core job-ready skills:
- SQL joins and aggregations
- Common table expressions (CTEs)
- Window functions
- Star schema fundamentals
- Query optimization and production patterns

## Learning Roadmap

Roadmap detail: `docs/roadmap.md`  
Roadmap checklist: `docs/roadmap_checklist.md`

### Phase Progress

- [x] Phase 1: Core Fundamentals (notebooks organized and runnable)
- [x] Phase 2: Practice Problems (weekly practice track active)
- [ ] Phase 3: Production Patterns (next milestone)

## Start Learning

1. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

2. Export PostgreSQL variables:
```bash
export PGHOST=localhost
export PGPORT=5432
export PGDATABASE=learning
export PGUSER=postgres
export PGPASSWORD=postgres
```

3. Open any notebook in `notebooks/` and run the first bootstrap cell.

## Recommended Notebook Order

1. `notebooks/01_core_fundamentals/00_basics/main.ipynb`
2. `notebooks/01_core_fundamentals/02_joins/basic.ipynb`
3. `notebooks/01_core_fundamentals/03_ctes/ctes.ipynb`
4. `notebooks/01_core_fundamentals/04_window_functions/window_functions.ipynb`
5. `notebooks/02_practice_problems/week_01/main.ipynb`

## Repository Structure

```text
.
├── .github/                     # CI, templates
├── data/                        # Tiny sample-only tracked data
├── docs/                        # Roadmap, checklist, repo strategy
├── notebooks/                   # SQL learning path
├── scripts/                     # Repo validation scripts
├── src/sql_for_analysis/        # Shared Python helpers
├── tests/                       # Unit/interface tests
├── CONTRIBUTING.md
├── README.md
└── requirements.txt
```

Detailed structure: `docs/project_structure.md`

## Validation

```bash
PYTHONPATH=src python3 -m pytest -q
python3 scripts/verify_notebook_imports.py
```

## GitHub Discoverability Checklist

See `docs/github_discoverability.md` for repo settings and publishing best practices (topics, release cadence, social preview, pinned roadmap updates).

## Data Policy

- Keep only lightweight sample data in `data/sample/`.
- Do not commit large/raw datasets or secrets.
