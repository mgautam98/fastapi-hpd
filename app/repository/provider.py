from fastapi import HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from app.database import db
from app import schemas
from uuid import UUID


def get_all():
    return [*db.values()]


def get(providerID: UUID):
    providerID: str = jsonable_encoder(providerID)
    provider = db[providerID]
    if not provider:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with providerID {str(providerID)} does not exists",
        )
    return provider


def create(request: schemas.HealthcareProviderBase):
    new_provider = jsonable_encoder(schemas.HealthcareProvider.from_orm(request))
    db[new_provider["providerID"]] = new_provider
    return new_provider


def update(providerID: UUID, request: schemas.HealthcareProviderBase):
    updated_provider = jsonable_encoder(schemas.HealthcareProvider.from_orm(request))
    providerID: str = jsonable_encoder(providerID)

    if not db[providerID]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with id {str(providerID)} does not exists",
        )

    updated_provider["providerID"] = providerID
    db[providerID] = updated_provider

    return Response(status_code=status.HTTP_204_NO_CONTENT)


def destroy(providerID: UUID):
    providerID: str = jsonable_encoder(providerID)
    if not db[providerID]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Health Provider with id {str(providerID)} does not exists",
        )
    db.pop(providerID)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
