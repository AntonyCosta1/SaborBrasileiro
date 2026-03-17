from fastapi import APIRouter

router = APIRouter()

router.get("/sales")
def sales_report():
    return {
        "total_sales": 0,
        "orders_count": 0
    }