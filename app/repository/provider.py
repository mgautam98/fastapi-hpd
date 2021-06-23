from fastapi import HTTPException, status, Response
from app.database import db
from app import schemas


def get_all():
    return db.db


def get(id: int):
    if not db.get(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with id {id}  does not exists')
    return db[id]


def create(request: schemas.HealthcareProvider):
    id: int = request.providerID
    if db.get(id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Health Provider with id {id} already exists')
    db[request.providerID] = (request.dict())
    return request


def update(id: int, request: schemas.HealthcareProvider):
    if not db.get(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with id {id}  does not exists')
    db[id] = (request.dict())
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def destroy(id: int):
    if not db.get(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Health Provider with id {id}  does not exists')
    db.pop(id, None)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
