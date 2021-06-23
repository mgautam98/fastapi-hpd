from fastapi import FastAPI
from app.routers import provider
from fastapi.openapi.utils import get_openapi


app = FastAPI()


app.include_router(provider.router)


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
