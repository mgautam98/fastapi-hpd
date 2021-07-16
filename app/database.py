import aiosql
from app.core.config import settings
from app.core.dataimp import FileDatabase
from app import main
import pathlib

db = FileDatabase(path=settings.DATABASE_PATH)

# db = DatabaseShelve(path=settings.DATABASE_PATH)

queries = aiosql.from_path(pathlib.Path(__file__).parent / "providers.sql", "psycopg2")


def get_connection():
    conn = main.app.state.pool.getconn()
    try:
        yield conn
    finally:
        main.app.state.pool.putconn(conn)
