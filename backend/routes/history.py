from fastapi import APIRouter
from backend.database.db import get_recent_chats, clear_chat_history

router = APIRouter(prefix="/api/history", tags=["History & Dashboard"])

@router.get("/")
async def get_history(limit: int = 20):
    return get_recent_chats(limit)

@router.delete("/clear")
async def clear_history():
    success = clear_chat_history()
    return {"success": success, "message": "Chat history cleared successfully."}
