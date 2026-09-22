import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env if present
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

AI_API_KEY = os.getenv("AI_API_KEY", "")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "auto")  # "gemini", "openai", or "auto"
DB_PATH = os.getenv("DB_PATH", str(BASE_DIR / "backend" / "nyaaya.db"))
PORT = int(os.getenv("PORT", "8000"))
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
