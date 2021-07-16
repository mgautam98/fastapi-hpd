from app.routers import provider
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from psycopg2 import pool

# ################
# FastAPI App
# ################

app = FastAPI()


origins = ["localhost"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_handler():
    """
    Creates pool of reusable connections
    for database
    """
    app.state.pool = pool.SimpleConnectionPool(
        1,
        20,
        host="localhost",
        port=5432,
        dbname="providers",
        user="root",
        password="root",
    )


@app.on_event("shutdown")
def shutdown_handler():
    """
    Closes all the database connections
    """
    app.state.pool.closeall


# ################
# Routing
# ################


app.include_router(provider.router, prefix="/api")

app.mount("/app", StaticFiles(directory="frontend/public", html=True), name="public")


@app.get("/")
def docs_redirect():
    return RedirectResponse(url="/app")


# ################
# Database
# ################


# def get_connection():
#     conn = app.state.pool.getconn()
#     try:
#         yield conn
#     finally:
#         app.state.pool.putconn(conn)


# ################
# OpenAPI specs
# ################


def openapi_specs():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Healthcare Provider Directory",
        version="0.0.1",
        description="OpenAPI Schemas",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = openapi_specs
