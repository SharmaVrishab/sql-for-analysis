"""PostgreSQL connection helper used across notebooks and exercises."""

from contextlib import contextmanager
import os

import psycopg2
from psycopg2 import Error

_REQUIRED_ENV_VARS = ["PGHOST", "PGPORT", "PGDATABASE", "PGUSER", "PGPASSWORD"]


def _load_config() -> dict:
    missing = [name for name in _REQUIRED_ENV_VARS if not os.getenv(name)]
    if missing:
        missing_text = ", ".join(missing)
        raise RuntimeError(
            f"Missing required PostgreSQL environment variables: {missing_text}"
        )

    return {
        "host": os.environ["PGHOST"],
        "port": os.environ["PGPORT"],
        "database": os.environ["PGDATABASE"],
        "user": os.environ["PGUSER"],
        "password": os.environ["PGPASSWORD"],
    }


@contextmanager
def get_connection():
    """Yield a psycopg2 connection and ensure it is always closed."""
    connection = None
    try:
        config = _load_config()
        connection = psycopg2.connect(**config)
        yield connection
    except RuntimeError:
        raise
    except (Exception, Error) as error:
        raise RuntimeError(f"PostgreSQL connection error: {error}") from error
    finally:
        if connection:
            connection.close()
