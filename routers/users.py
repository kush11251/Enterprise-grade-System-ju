from fastapi import APIRouter, HTTPException
from services import users_service
router = APIRouter()
@router.get("/users")
def get_users():
    return users_service.get_users()