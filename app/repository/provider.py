from fastapi import HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from app.core.utils import get_all_keys, build_dictionary
from app.database import db, queries, get_connection
from app import schemas
from uuid import UUID


conn = get_connection()


def get_all(skip: int, limit: int):
    return [*db.values()][skip : skip + limit]


def get(providerID: UUID):
    providerID: str = jsonable_encoder(providerID)
    provider = db.find(providerID)
    if not provider:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with providerID {str(providerID)} does not exists",
        )
    return provider


def create(request: schemas.HealthcareProviderBase):
    new_provider = jsonable_encoder(schemas.HealthcareProvider.from_orm(request))
    db.add(new_provider)
    return new_provider


def update(providerID: UUID, request: schemas.HealthcareProviderBase):
    updated_provider = jsonable_encoder(schemas.HealthcareProvider.from_orm(request))
    providerID: str = jsonable_encoder(providerID)

    if not db.find(providerID):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with id {str(providerID)} does not exists",
        )

    updated_provider["providerID"] = providerID
    db.update(providerID, updated_provider)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def destroy(providerID: UUID):
    providerID: str = jsonable_encoder(providerID)
    if not db.find(providerID):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with id {str(providerID)} does not exists",
        )
    db.delete(providerID)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def search(request: schemas.SearchRequest):
    with get_connection() as conn:
        results_values = queries.search_providers(
            conn, query=request.term, limit=request.limit, offset=request.offset
        )
    results_dict = build_dictionary(get_all_keys, results_values)
    return results_dict
