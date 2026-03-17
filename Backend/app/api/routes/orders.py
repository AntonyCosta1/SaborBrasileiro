from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter()

@router.get("/my", response_model=list[OrderResponse])
def my_orders(db: Session = Depends(get_db)):
    return 
        db.query(Order).all()

@router.post("/", response_model=OrderResponse)
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(
        user_id = order_data.user_id
        payment_method = order_data.payment_method,
        subtotal = order_data.subtotal,
        delivery_fee = order_data.delivery_fee,
        total = order_data.total
        status = "pending",
        payment_status = "pending"

    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order