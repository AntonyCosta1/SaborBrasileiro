from pydantic import BaseModel
from datetime import datetime

class MenuItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None
    active: bool = True

class MenuItemResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True