from fastapi import FastAPI
from app.routers import provider


app = FastAPI()


app.include_router(provider.router)
