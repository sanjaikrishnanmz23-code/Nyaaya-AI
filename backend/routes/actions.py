from fastapi import APIRouter, HTTPException
from backend.services.actions_data import get_all_action_guides, get_action_guide_by_id

router = APIRouter(prefix="/api/actions", tags=["What Should I Do"])

@router.get("/problems")
async def list_problems():
    return get_all_action_guides()

@router.get("/{problem_id}")
async def get_problem(problem_id: str):
    guide = get_action_guide_by_id(problem_id)
    if not guide:
        raise HTTPException(status_code=404, detail="Problem guide not found.")
    return guide
