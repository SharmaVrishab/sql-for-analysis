from contextlib import contextmanager
import psycopg2
from psycopg2 import Error

@contextmanager
def get_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="learning",
            user="postgres",
            password="postgres",
            port="5432",
        )
        yield connection

    except (Exception, Error) as error:
        raise RuntimeError(f"PostgreSQL connection error: {error}")

    finally:
        if connection:
            connection.close()
