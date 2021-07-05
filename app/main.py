from app.routers import provider
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

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

# ################
# Routing
# ################


app.include_router(provider.router, prefix="/api")

app.mount("/app", StaticFiles(directory="frontend/public", html=True), name="public")


@app.get("/")
def docs_redirect():
    return RedirectResponse(url="/app")


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
