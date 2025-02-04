from pydantic import BaseModel, EmailStr, Field
from typing import List

class ContactRequest(BaseModel):
    email: EmailStr
    phone: int  

    class Config:
        orm_mode = True

class ContactResponse(BaseModel):
    contact_ids: List[int] = Field(..., alias="contactIds")
    emails: List[str]
    phones: List[int]

    class Config:
        allow_population_by_field_name = True


