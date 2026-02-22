# SQL for Data Engineering Learning Roadmap

This roadmap is designed for practical, interview-relevant SQL development.

## Phase 1: Core Fundamentals

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

## Phase 2: Practice Problems

Goal: Improve speed, accuracy, and query readability under problem-solving constraints.

- Weekly SQL drills
- Query refactoring
- Tradeoff discussion between readability and performance

Primary notebook:
- `notebooks/02_practice_problems/week_01/main.ipynb`

## Phase 3: Production Patterns

Goal: Move from learning SQL syntax to shipping reliable SQL pipelines.

- Incremental loading patterns
- Idempotent query design
- Deduplication strategies
- Data quality checks
- Query performance analysis

Status: Planned and tracked in `docs/roadmap_checklist.md`.
