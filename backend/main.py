import os
from pathlib import Path
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.config import PORT, DEBUG
from backend.database.db import init_db
from backend.routes.chat import router as chat_router
from backend.routes.rights import router as rights_router
from backend.routes.services import router as services_router
from backend.routes.actions import router as actions_router
from backend.routes.emergency import router as emergency_router
from backend.routes.history import router as history_router
from backend.services.rights_data import get_all_categories
from backend.services.services_data import get_all_services
from backend.services.actions_data import get_all_action_guides
from backend.services.emergency_data import get_all_emergency_contacts

# Initialize database tables
init_db()

app = FastAPI(
    title="NyaayaAI – Citizen Rights Information API",
    description="Generative AI & Knowledge Engine for Indian Citizen Rights, Statutory Remedies, and Public Services (English + Tamil)",
    version="1.0.0"
)

# Enable CORS for frontend Vite development server and production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(chat_router)
app.include_router(rights_router)
app.include_router(services_router)
app.include_router(actions_router)
app.include_router(emergency_router)
app.include_router(history_router)

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "NyaayaAI",
        "tagline": "Know Your Rights. Know Your Voice.",
        "bilingual_support": ["English", "Tamil (தமிழ்)"],
        "version": "1.0.0"
    }

@app.get("/api/search")
async def global_search(q: str = Query(..., min_length=1)):
    """Unified global instant search across rights, services, and action guides."""
    query = q.strip().lower()
    
    matched_rights = []
    for cat in get_all_categories():
        if (query in cat["title"].lower() or 
            query in cat["title_tamil"].lower() or 
            query in cat["short_desc"].lower() or 
            query in cat["badge"].lower()):
            matched_rights.append({
                "type": "right",
                "id": cat["id"],
                "title": cat["title"],
                "title_tamil": cat["title_tamil"],
                "desc": cat["short_desc"]
            })
            
    matched_services = []
    for srv in get_all_services():
        if (query in srv["title"].lower() or 
            query in srv["title_tamil"].lower() or 
            query in srv["description"].lower() or 
            query in srv["category"].lower()):
            matched_services.append({
                "type": "service",
                "id": srv["id"],
                "title": srv["title"],
                "title_tamil": srv["title_tamil"],
                "desc": srv["description"]
            })
            
    matched_actions = []
    for act in get_all_action_guides():
        if (query in act["title"].lower() or 
            query in act["title_tamil"].lower() or 
            query in act["summary"].lower()):
            matched_actions.append({
                "type": "action",
                "id": act["id"],
                "title": act["title"],
                "title_tamil": act["title_tamil"],
                "desc": act["summary"]
            })

    return {
        "query": q,
        "results": {
            "rights": matched_rights,
            "services": matched_services,
            "actions": matched_actions
        },
        "total": len(matched_rights) + len(matched_services) + len(matched_actions)
    }

# Mount frontend static distribution if built
dist_dir = Path(__file__).resolve().parent.parent / "frontend" / "dist"
if dist_dir.exists():
    app.mount("/", StaticFiles(directory=str(dist_dir), html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=PORT, reload=DEBUG)
