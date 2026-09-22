from fastapi import APIRouter, HTTPException
from backend.models.schemas import ChatRequest, StructuredAnswer
from backend.services.ai_service import ai_service_instance
from backend.database.db import save_chat

router = APIRouter(prefix="/api/chat", tags=["Chat"])

@router.post("/", response_model=StructuredAnswer)
async def ask_question(request: ChatRequest):
    if not request.question or not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    answer = ai_service_instance.query(request.question, request.language)
    
    # Save to SQLite database
    try:
        save_chat(
            session_id=request.session_id or "default-session",
            question=request.question,
            language=request.language,
            response_dict=answer.model_dump()
        )
    except Exception as e:
        # Non-fatal error for logging
        print(f"Error persisting chat history: {e}")
        
    return answer
