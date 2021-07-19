from fastapi import HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from app.core.utils import build_providers, build_provider
from app.database import db, queries, get_connection
from app import schemas
from uuid import UUID


def get_all(skip: int, limit: int):
    with get_connection() as conn:
        results_values = queries.get_all_providers(conn, limit=limit, offset=skip)
    results_dict = build_providers(results_values)
    return results_dict


def get(providerID: UUID):
    providerID: str = jsonable_encoder(providerID)
    with get_connection() as conn:
        provider = queries.get_provider_by_id(conn, providerid=providerID)
        phone_number = queries.get_phone_by_provider_id(conn, providerid=providerID)
        specialities = queries.get_speclialty_by_provider_id(
            conn, providerid=providerID
        )
        qualifications = queries.get_qualification_by_provider_id(
            conn, providerid=providerID
        )
    if len(provider) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with providerID {str(providerID)} does not exists",
        )
    provider_dict = build_provider(provider, phone_number, qualifications, specialities)
    return provider_dict


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
    results_dict = build_providers(results_values)
    return results_dict
