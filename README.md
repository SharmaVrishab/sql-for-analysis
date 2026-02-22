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

### Phase 1: Core Fundamentals

Goal: Build fluency in SQL building blocks and analytics query patterns.

- Basic SQL query flow (`SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`)
- JOIN patterns and duplicate handling
- CTE structuring
- Window functions (`ROW_NUMBER`, `RANK`, `LAG`, `LEAD`)
- Star schema basics

Primary notebooks:
- `notebooks/01_core_fundamentals/00_basics/main.ipynb`
- `notebooks/01_core_fundamentals/02_joins/basic.ipynb`
- `notebooks/01_core_fundamentals/03_ctes/ctes.ipynb`
- `notebooks/01_core_fundamentals/04_window_functions/window_functions.ipynb`

### Phase 2: Practice Problems

Goal: Improve speed, accuracy, and query readability under problem-solving constraints.

- Weekly SQL drills
- Query refactoring
- Tradeoff discussion between readability and performance

Primary notebook:
- `notebooks/02_practice_problems/week_01/main.ipynb`

### Phase 3: Production Patterns

Goal: Move from learning SQL syntax to shipping reliable SQL pipelines.

- Incremental loading patterns
- Idempotent query design
- Deduplication strategies
- Data quality checks
- Query performance analysis

## Phase Progress

- [x] Phase 1: Core Fundamentals
- [x] Phase 2: Practice Problems
- [ ] Phase 3: Production Patterns

## Roadmap Checklist

- [x] Basic SQL notebook completed
- [x] JOIN notebook completed
- [x] CTE notebook completed
- [x] Window functions notebook completed
- [x] Star schema notebook completed
- [x] Week 1 practice notebook added
- [ ] Week 2 practice notebook added
- [ ] Week 3 practice notebook added
- [ ] Add production-pattern notebooks

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
├── notebooks/                   # SQL learning path
├── scripts/                     # Repo validation scripts
├── src/sql_for_analysis/        # Shared Python helpers
├── tests/                       # Unit/interface tests
├── CONTRIBUTING.md
├── README.md
└── requirements.txt
```
