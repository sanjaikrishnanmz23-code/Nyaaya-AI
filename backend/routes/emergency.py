from fastapi import APIRouter
from backend.services.emergency_data import get_all_emergency_contacts

router = APIRouter(prefix="/api/emergency", tags=["Emergency Helplines"])

@router.get("/contacts")
async def list_emergency_contacts():
    return get_all_emergency_contacts()
