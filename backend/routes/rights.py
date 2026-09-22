from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from backend.services.rights_data import get_all_categories, get_category_by_id

router = APIRouter(prefix="/api/rights", tags=["Rights Explorer"])

@router.get("/categories")
async def list_categories():
    return get_all_categories()

@router.get("/{category_id}")
async def get_category(category_id: str):
    cat = get_category_by_id(category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Rights category not found.")
    return cat

@router.get("/search/")
async def search_rights(q: str = Query(..., min_length=1)):
    query = q.strip().lower()
    categories = get_all_categories()
    results = []
    
    for cat in categories:
        matched = False
        if query in cat["title"].lower() or query in cat["title_tamil"].lower() or query in cat["short_desc"].lower():
            matched = True
        else:
            for q_item in cat.get("common_questions", []):
                if query in q_item.get("q", "").lower() or query in q_item.get("q_ta", "").lower():
                    matched = True
                    break
        if matched:
            results.append(cat)
            
    return results
