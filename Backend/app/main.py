from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.model import user, menu_item, order, payment
from app.api.routes import auth, menu, orders, admin, payments, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sabor Brasileiro API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(menu.router, prefix="/menu", tags=["menu"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/health")
def heath_check():
    return {"status": "ok"}