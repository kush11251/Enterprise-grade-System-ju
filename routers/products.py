from fastapi import APIRouter, HTTPException
from services import products_service
router = APIRouter()
@router.get("/products")
def get_products():
    return products_service.get_products()