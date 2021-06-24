from app.core.config import settings
from app.core.dataimp import FileDatabase


db = FileDatabase(path=settings.DATABASE_PATH)

# db = DatabaseShelve(path=settings.DATABASE_PATH)
