from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: int
    payment_method: str | None = None
    subtotal: float
    delivery_fee: float = 0
    total: float

class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: str
    payment_status: str
    payment_method: str | None = None
    subtotal: float
    delivery_fee: float
    total: float
    created_at: datetime

    class Config:
        from_attributes = True
        