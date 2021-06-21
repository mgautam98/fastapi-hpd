from pydantic import BaseModel
from typing import Optional, List


class HealthcareProvider(BaseModel):
    providerID: int
    active: Optional[bool] = True
    name: str
    qualification: List[str]
    speciality: List[str]
    phone: List[str]
    department: Optional[str] = None
    organization: str
    location: Optional[str] = None
    address: str
