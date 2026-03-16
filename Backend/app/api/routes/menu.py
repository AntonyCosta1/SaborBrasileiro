from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_menu():
    return [
        {"id": 1, "name": "Feijoada", "price": 25.0},
        {"id": 2, "name": "Picanha", "price": 40.0},
    ]