from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID, uuid4


class HealthcareProviderBase(BaseModel):
    active: Optional[bool] = True
    name: str
    qualification: List[str]
    speciality: List[str]
    phone: List[str]
    department: Optional[str] = None
    organization: str
    location: Optional[str] = None
    address: str


class HealthcareProvider(BaseModel):
    providerID: UUID = Field(default_factory=uuid4)
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
