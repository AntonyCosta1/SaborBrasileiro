from fastapi import APIRouter

router = APIRouter()

@router.post("/pix")
def create_pix_payment():
    return {
        "message": "Pagamento via Pix criado com sucesso",
        "qr_code": "examplo_qr_code",
        "pix_copy_paste": "000201..."
        }