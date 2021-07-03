from pydantic import BaseModel, Field, constr, validator
from typing import Optional, List
from uuid import UUID, uuid4
from re import compile


phone_regex = compile(
    r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$"
)


class HealthcareProviderBase(BaseModel):
    active: Optional[bool] = True
    name: constr(min_length=2, max_length=40)
    qualification: List[str]
    speciality: List[str]
    phone: List[str]
    department: Optional[str] = None
    organization: str
    location: Optional[str] = None
    address: str

    @validator("phone", each_item=True)
    def validate_phone(cls, v):
        if not phone_regex.search(v):
            raise ValueError("Not valid phone number")
        return v


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

    @validator("phone", each_item=True)
    def validate_phone(cls, v):
        if not phone_regex.search(v):
            raise ValueError("Not valid phone number")
        return v

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
