# Project Structure

## notebooks/

- `00_setup/`: notebook bootstrap helper.
- `01_core_fundamentals/`: foundation learning track.
- `02_practice_problems/`: weekly practice notebooks.
- `99_extras/`: supporting utility notebooks.

## src/sql_for_analysis/

- `db/connection.py`: shared PostgreSQL connection context manager.

## scripts/

- `verify_notebook_imports.py`: enforces shared import contract in notebooks.

## tests/

- `test_db_connection_interface.py`: interface and failure-mode checks for DB connection helper.

## data/

- `sample/`: tiny tracked data examples only.
