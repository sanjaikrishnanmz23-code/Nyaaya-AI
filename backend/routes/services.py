from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from backend.services.services_data import get_all_services, get_service_by_id

router = APIRouter(prefix="/api/services", tags=["Government Services"])

@router.get("/")
async def list_services(category: Optional[str] = None, q: Optional[str] = None):
    services = get_all_services()
    if category and category.lower() != "all":
        services = [s for s in services if category.lower() in s["category"].lower()]
    if q and q.strip():
        query = q.strip().lower()
        services = [
            s for s in services 
            if query in s["title"].lower() 
            or query in s["title_tamil"].lower() 
            or query in s["description"].lower()
            or query in s["relevant_authority"].lower()
        ]
    return services

@router.get("/{service_id}")
async def get_service(service_id: str):
    srv = get_service_by_id(service_id)
    if not srv:
        raise HTTPException(status_code=404, detail="Service not found.")
    return srv
