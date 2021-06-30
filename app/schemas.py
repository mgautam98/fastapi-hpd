from pydantic import BaseModel, Field, constr, validator, ValidationError
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
    name: constr(min_length=2, max_length=40)
    qualification: List[str]
    speciality: List[str]
    phone: List[str]
    department: Optional[str] = None
    organization: str
    location: Optional[str] = None
    address: str

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "providerID": "providerID",
                "active": True,
                "name": "string",
                "qualification": ["string"],
                "speciality": ["string"],
                "phone": ["string"],
                "department": "string",
                "organization": "string",
                "location": "string",
                "address": "string",
            }
        }
