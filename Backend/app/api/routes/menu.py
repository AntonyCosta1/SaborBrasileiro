from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.menu_item import MenuItem
from app.schemas.menu_item import MenuItemCreate, MenuItemResponse

router = APIRouter()

@router.get("/", response_model=list[MenuItemResponse])
def list_menu(db: Session = Depends(det_db)):
    return 
        db.query(MenuItem).filter(MenuItem.active == True).all()

@router.post("/", response_model=MenuItemResponse)
def create_menu_item(item_data: MenuItemCreate, db: Session = Depends(get_db)):
    new_item = MenuItem(
        name = item_data.name,
        description = item_data.description,
        price = item_data.price,
        image_url = item_data.image_url,
        active = item_data.active
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item
