import sqlite3
import json
from pathlib import Path
from backend.config import DB_PATH

def get_connection():
    db_file = Path(DB_PATH)
    db_file.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Chat queries and responses history
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        question TEXT NOT NULL,
        language TEXT NOT NULL,
        response_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Saved bookmarks
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookmarks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id TEXT NOT NULL,
        item_type TEXT NOT NULL, -- 'chat_answer', 'right', 'service', 'action'
        title TEXT NOT NULL,
        data_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(item_id, item_type)
    )
    """)

    # Recent search queries
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recent_searches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        category TEXT DEFAULT 'all',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # User preferences
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_preferences (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def save_chat(session_id: str, question: str, language: str, response_dict: dict) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_history (session_id, question, language, response_json) VALUES (?, ?, ?, ?)",
        (session_id, question, language, json.dumps(response_dict, ensure_ascii=False))
    )
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id

def get_recent_chats(limit: int = 20):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, session_id, question, language, response_json, created_at FROM chat_history ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    results = []
    for r in rows:
        results.append({
            "id": r["id"],
            "session_id": r["session_id"],
            "question": r["question"],
            "language": r["language"],
            "response": json.loads(r["response_json"]),
            "created_at": r["created_at"]
        })
    return results

def clear_chat_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat_history")
    cursor.execute("DELETE FROM recent_searches")
    conn.commit()
    conn.close()
    return True
