from fastapi import APIRouter, status
from app import schemas
from app.repository import provider
from typing import List
from uuid import UUID

router = APIRouter(prefix="/provider", tags=["Healthcare Providers"])


@router.get("/", response_model=List[schemas.HealthcareProviderMin])
def get_all(skip: int = 0, limit: int = 10):
    return provider.get_all(skip, limit)


@router.get("/{providerID}", response_model=schemas.HealthcareProvider)
def get(providerID: UUID):
    return provider.get(providerID)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.HealthcareProvider
)
def add(request: schemas.HealthcareProviderBase):
    return provider.create(request)


@router.put("/{providerID}", status_code=status.HTTP_204_NO_CONTENT)
def update(providerID: UUID, request: schemas.HealthcareProviderBase):
    return provider.update(providerID, request)


@router.delete("/{providerID}", status_code=status.HTTP_204_NO_CONTENT)
def delete(providerID: UUID):
    return provider.destroy(providerID)


@router.post("/search", response_model=List[schemas.HealthcareProviderMin])
def search(request: schemas.SearchRequest):
    return provider.search(request)
