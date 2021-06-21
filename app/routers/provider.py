from app import schemas
from app.database import db
from fastapi import APIRouter, status, HTTPException

router = APIRouter(
    prefix='/provider',
    tags=['Healthcare Providers']
)


@router.get('/')
def get_all():
    return db


@router.get('/{id}')
def get(id: int):
    if not db.get(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with id {id}  does not exists')
    return db[id]


@router.post('/', status_code=status.HTTP_201_CREATED)
def add(request: schemas.HealthcareProvider):
    id: int = request.providerID
    if db.get(id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Health Provider with id {id} already exists')
    db[request.providerID] = (request.dict())
    return request


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.HealthcareProvider):
    if not db.get(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with id {id}  does not exists')
    db[id] = request


@router.delete('/{id}', status_code=status.HTTP_201_CREATED)
def delete(id: int):
    if not db.get(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with id {id}  does not exists')
    db.pop(id, None)
    return {'task': 'deletion sucessful!'}
