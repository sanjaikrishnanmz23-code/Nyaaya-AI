from typing import List, Optional
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    question: str
    language: str = Field(default="both", description="Language mode: 'en', 'ta', or 'both'")
    session_id: Optional[str] = "default-session"

class SourceInfo(BaseModel):
    source_type: str = "Official Legal Information / Statutory Code"
    source_name: str
    legal_section: Optional[str] = None
    last_verified: str = "September 2024 / Demo Data"
    verify_url: Optional[str] = None
    verification_note: Optional[str] = "Demo Source – Verify with official Gazette or statutory authority before legal proceedings."

class StructuredAnswer(BaseModel):
    question: str
    simple_explanation: str
    what_you_can_do: List[str]
    your_rights: List[str]
    where_to_get_help: List[str]
    tamil_explanation: str
    tamil_steps: List[str] = []
    disclaimer: str = "Information provided for educational purposes. Laws and procedures may change. Verify important matters with official government/legal sources."
    sources: List[SourceInfo] = []
    category: Optional[str] = "General Citizen Rights"
    suggested_followups: List[str] = []

class RightsCategory(BaseModel):
    id: str
    title: str
    title_tamil: str
    icon: str
    short_desc: str
    short_desc_tamil: str
    badge: str
    overview: str
    overview_tamil: str
    common_questions: List[dict]
    citizen_actions: List[str]
    citizen_actions_tamil: List[str]
    relevant_authorities: List[str]
    important_documents: List[str]
    official_sources: List[SourceInfo]

class GovernmentService(BaseModel):
    id: str
    title: str
    title_tamil: str
    category: str
    icon: str
    description: str
    description_tamil: str
    eligibility: List[str]
    required_documents: List[str]
    step_by_step_process: List[str]
    relevant_authority: str
    official_portal_name: str
    official_url_demo: str
    processing_time: str
    fee_structure: str

class ProblemActionGuide(BaseModel):
    id: str
    title: str
    title_tamil: str
    icon: str
    urgency_level: str  # High, Medium, Standard
    summary: str
    summary_tamil: str
    timeline_steps: List[dict]  # step_title, step_desc, actions, timing
    do_this_first: List[str]
    do_next: List[str]
    then_step: List[str]
    follow_up: List[str]
    helpline: Optional[str] = None
    helpline_name: Optional[str] = None
    documents_checklist: List[str]

class EmergencyContact(BaseModel):
    id: str
    name: str
    name_tamil: str
    number: str
    category: str
    description: str
    description_tamil: str
    available_24_7: bool
