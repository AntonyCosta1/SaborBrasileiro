from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def admin_dashboard():
    return {
        "total_vendas_dia": 0,
        "total_vendas_mes": 0,
        "total_pedidos": 0
    }