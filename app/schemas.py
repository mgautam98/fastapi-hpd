from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


class HealthcareProvider(BaseModel):
    active: Optional[bool] = True
    name: str
    qualification: List[str]
    speciality: List[str]
    phone: List[str]
    department: Optional[str] = None
    organization: str
    location: Optional[str] = None
    address: str


class HealthcareProviderShow(BaseModel):
    providerID: UUID
    active: Optional[bool] = True
    name: str
    qualification: List[str]
    speciality: List[str]
    phone: List[str]
    department: Optional[str] = None
    organization: str
    location: Optional[str] = None
    address: str

    class Config():
        orm_mode = True
