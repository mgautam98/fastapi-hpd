from fastapi import HTTPException, status, Response
from app.database import db
from app import schemas
from uuid import UUID


def get_all():
    return db.db


def get(providerID: UUID):
    if not db.get(providerID):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with providerID {str(providerID)} does not exists')
    return db[providerID]


def create(request: schemas.HealthcareProviderBase):
    new_provider = schemas.HealthcareProvider.from_orm(request)
    db[new_provider.providerID] = (new_provider.dict())
    return new_provider


def update(providerID: UUID, request: schemas.HealthcareProvider):
    if providerID != request.providerID:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    if not db.get(providerID):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with id {str(providerID)} does not exists')
    db[providerID] = (request.dict())
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def destroy(providerID: UUID):
    if not db.get(providerID):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with id {str(providerID)} does not exists')
    db.pop(providerID, None)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
