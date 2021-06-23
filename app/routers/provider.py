from fastapi import APIRouter, status
from app import schemas
from app.repository import provider
from uuid import UUID

router = APIRouter(
    prefix='/provider',
    tags=['Healthcare Providers']
)


@router.get('/')
def get_all():
    return provider.get_all()


@router.get('/{providerID}', response_model=schemas.HealthcareProvider)
def get(providerID: UUID):
    return provider.get(providerID)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.HealthcareProvider)
def add(request: schemas.HealthcareProviderBase):
    return provider.create(request)


@router.put('/{providerID}', status_code=status.HTTP_204_NO_CONTENT)
def update(providerID: UUID, request: schemas.HealthcareProvider):
    return provider.update(providerID, request)


@router.delete('/{providerID}', status_code=status.HTTP_204_NO_CONTENT)
def delete(providerID: UUID):
    return provider.destroy(providerID)
