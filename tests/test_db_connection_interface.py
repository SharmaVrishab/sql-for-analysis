import os

import pytest

from sql_for_analysis.db.connection import get_connection


@pytest.mark.parametrize("name", ["PGHOST", "PGPORT", "PGDATABASE", "PGUSER", "PGPASSWORD"])
def test_get_connection_missing_env_vars_raises(name):
    original = {k: os.environ.get(k) for k in ["PGHOST", "PGPORT", "PGDATABASE", "PGUSER", "PGPASSWORD"]}
    for key in original:
        os.environ.pop(key, None)

    with pytest.raises(RuntimeError, match="Missing required PostgreSQL environment variables"):
        with get_connection():
            pass

    for key, value in original.items():
        if value is not None:
            os.environ[key] = value
