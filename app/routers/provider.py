from fastapi import APIRouter, status
from app import schemas
from app.repository import provider

router = APIRouter(
    prefix='/provider',
    tags=['Healthcare Providers']
)


@router.get('/')
def get_all():
    return provider.get_all()


@router.get('/{id}')
def get(id: int):
    return provider.get(id)


@router.post('/', status_code=status.HTTP_201_CREATED)
def add(request: schemas.HealthcareProvider):
    return provider.create(request)


@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update(id: int, request: schemas.HealthcareProvider):
    return provider.update(id, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    return provider.destroy(id)
