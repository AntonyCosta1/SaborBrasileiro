from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = none
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None = none
    role: str
    created_at: datetime

    class Config:
        from_attributes = True