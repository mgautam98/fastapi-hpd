from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PATH = './database.json'

    class Config:
        case_sensitive = True


settings = Settings()
