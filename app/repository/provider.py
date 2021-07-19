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
    providerID: str = jsonable_encoder(providerID)

    with get_connection() as conn:
        provider = queries.get_provider_by_id(conn, providerid=providerID)

    if len(provider) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with id {str(providerID)} does not exists",
        )

    with get_connection() as conn:
        provider_status = queries.update_provider(
            conn,
            active=request.active,
            name=request.name,
            organization=request.organization,
            address=request.address,
            department=request.department,
            location=request.location,
            providerid=providerID,
        )
        for phone in request.phone:
            queries.update_phone_numbers(conn, phone=phone, providerid=providerID)

        for qualification in request.qualification:
            queries.update_qualifications(
                conn, qualification=qualification, providerid=providerID
            )

        for speciality in request.speciality:
            queries.update_specialities(
                conn, speciality=speciality, providerid=providerID
            )

    if len(provider_status) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error updating Health Provider with id {str(providerID)}",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


def destroy(providerID: UUID):
    providerID: str = jsonable_encoder(providerID)

    with get_connection() as conn:
        deleted_id = queries.delete_provider_by_id(conn, providerid=providerID)

    if len(deleted_id) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with id {str(providerID)} does not exists",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def search(request: schemas.SearchRequest):
    with get_connection() as conn:
        results_values = queries.search_providers(
            conn, query=request.term, limit=request.limit, offset=request.offset
        )
    results_dict = build_providers(results_values)
    return results_dict
