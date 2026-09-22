# NyaayaAI – Citizen Rights Info
### *“Know Your Rights. Know Your Voice.”*
### *“உங்கள் உரிமைகளை அறிந்திடுங்கள். உங்கள் குரலை ஓங்கிடுங்கள்.”*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/Frontend-React%2018-61DAFB.svg?logo=react&logoColor=black)](https://reactjs.org)
[![TailwindCSS](https://img.shields.io/badge/Styling-Tailwind%20CSS-38B2AC.svg?logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![Bilingual](https://img.shields.io/badge/Language-English%20%7C%20%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D-cyan)](https://github.com/sanjaikrishnanmz23-code/Nyaaya-AI)

NyaayaAI is a modern Generative AI & Knowledge-powered Citizen Rights Information Assistant designed specifically for Indian citizens. It explains complex constitutional protections, statutory remedies, police protocols, consumer rights, and public services in simple, practical, bilingual language (**English and Tamil / தமிழ்**).

---

## Key Features

1. **Bilingual Generative AI Chat Engine (English & தமிழ்)**
   - Instant structured answers for citizen questions:
     - Simple Jargon-Free Explanation
     - Actionable, Numbered Steps (*What You Can Do*)
     - Relevant Statutory Rights & Constitutional Provisions (*Your Rights*)
     - Designated Authorities & Redressal Portals (*Where to Get Help*)
     - Natural, Fluent Tamil Explanation (*தமிழ் விளக்கம்*)
     - Verified Statutory Sources & Public Authority Citations
   - Integrated Web Speech API for **Voice Input** and bilingual **Text-To-Speech (TTS)**.
   - Dedicated language switchers: `[ English ]` `[ தமிழ் ]` `[ Both / இரண்டும் ]`.

2. **Citizen Rights Explorer (10 Comprehensive Categories)**
   - Fundamental Rights (Articles 14–32)
   - Labour & Worker Rights (Payment of Wages Act, Minimum Wages, Samadhan Portal)
   - Consumer Rights (Consumer Protection Act 2019, e-Daakhil, MRP violations)
   - Police & Legal Protections (D.K. Basu guidelines, FIR registration, Section 41/50 CrPC/BNSS, Bail)
   - Digital & Privacy Rights (IT Act 2000, 1930 Cyber Fraud freeze, DPDP Act)
   - Women & Child Rights (Domestic Violence Act, POSH Act, Sakhi One-Stop Centres)
   - Government Transparency & RTI (RTI Act 2005, 30-day timeline, First Appeals)
   - Education Rights (RTE Act 2009, 25% EWS reservation, Anti-Ragging)
   - Healthcare Rights (Patients' Charter, emergency care without advance deposit)
   - Environmental Rights (Article 21 clean environment, National Green Tribunal)

3. **Government Services Directory**
   - Step-by-step guides, eligibility, and document checklists for:
     - Aadhaar Card (UIDAI)
     - PAN Card (NSDL / UTIITSL)
     - Passport Seva (Tatkaal / Normal)
     - Voter Registration (ECI Form 6 / e-EPIC)
     - Driving Licence & LLR (Parivahan Sarathi)
     - e-District Certificates (Income, Community, Nativity)
     - Public Grievances (CPGRAMS)
     - RTI Online Filing

4. **“I Have a Problem. What Can I Do?” Guided Solver**
   - Interactive 4-stage progressive roadmap for crisis situations:
     - **Do this first → Next → Then → Follow up**
   - Covers: Salary Withheld, Online Banking Fraud, Consumer Disputes, Police Stops, and Bribe Demands.

5. **Verified Emergency Helplines Matrix**
   - Emergency All-in-One: `112`
   - Cyber Financial Fraud: `1930`
   - Women in Distress: `181 / 1091`
   - National Consumer Helpline: `1915`
   - Child Helpline: `1098`
   - Free Legal Aid (NALSA): `15100`
   - Senior Citizens: `14567`
   - Anti-Corruption / Vigilance: `1064`

6. **Futuristic Civic-Tech UI & VFX**
   - Deep Navy theme (`#060A14`), Electric Blue, and Cyan Glow.
   - Glassmorphism cards with subtle border radiance.
   - Canvas-based dynamic particle mesh background.
   - 3D Animated Glowing AI Orb with concentric orbital rings.
   - Global instant search (`Ctrl+K`).
   - Local privacy dashboard (no tracking, clearable query history).

---

## Tech Stack

- **Frontend**: React 18, Vite, Tailwind CSS, Lucide Icons, Web Speech API.
- **Backend**: Python 3, FastAPI, Uvicorn, Pydantic, SQLite3, python-dotenv.
- **AI Layer**: Extensible `AIService` supporting live LLM API keys (`AI_API_KEY`) with a statutory semantic knowledge base.

---

## Project Structure

```
Nyaaya-AI/
├── backend/
│   ├── config.py                 # Environment and application settings
│   ├── main.py                   # FastAPI app entry point, CORS, and routers
│   ├── database/
│   │   └── db.py                 # SQLite persistence for chat & search history
│   ├── models/
│   │   └── schemas.py            # Pydantic request and response schemas
│   ├── routes/
│   │   ├── chat.py               # AI query endpoints
│   │   ├── rights.py             # 10 Rights categories endpoints
│   │   ├── services.py           # Government services endpoints
│   │   ├── actions.py            # Guided problem solver endpoints
│   │   ├── emergency.py          # Emergency helplines endpoints
│   │   └── history.py            # Chat history and clear endpoints
│   └── services/
│       ├── ai_service.py         # Bilingual AI semantic reasoning engine
│       ├── rights_data.py        # Statutory rights database
│       ├── services_data.py      # Government services database
│       ├── actions_data.py       # Problem resolution workflows
│       └── emergency_data.py     # Verified helplines matrix
├── frontend/
│   ├── index.html                # HTML entry point with Google Fonts
│   ├── package.json              # Frontend npm dependencies
│   ├── vite.config.js            # Vite configuration and API proxy
│   ├── tailwind.config.js        # Design system tokens and keyframes
│   ├── src/
│   │   ├── App.jsx               # Main React application component
│   │   ├── index.css             # Glassmorphism utilities and styles
│   │   ├── main.jsx              # React DOM render entry
│   │   ├── components/
│   │   │   ├── AIOrb.jsx         # 3D Animated AI Orb with civic badges
│   │   │   ├── Footer.jsx        # Civic footer and legal disclaimer
│   │   │   ├── GlobalSearchModal.jsx # Ctrl+K instant search
│   │   │   ├── LanguageSelector.jsx  # EN / TA / Both selector
│   │   │   ├── Navbar.jsx        # Glassmorphic navigation header
│   │   │   ├── ParticleField.jsx # Canvas interactive particle mesh
│   │   │   └── SourceCard.jsx    # Statutory trust & verification modal
│   │   ├── pages/
│   │   │   ├── ActionGuidePage.jsx   # "What Should I Do?" guided roadmap
│   │   │   ├── ChatPage.jsx          # Main bilingual AI chat assistant
│   │   │   ├── DashboardPage.jsx     # Query history & saved bookmarks
│   │   │   ├── EmergencyPage.jsx     # Verified national helplines
│   │   │   ├── LandingPage.jsx       # Hero landing page
│   │   │   ├── RightsExplorer.jsx    # 10 Rights categories explorer
│   │   │   └── ServicesDirectory.jsx # Public services directory
│   │   ├── services/
│   │   │   └── api.js            # REST API client
│   │   └── utils/
│   │       └── speech.js         # Bilingual Text-to-Speech & Speech Recognition
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Prerequisites
- **Python 3.10+**
- **Node.js 18+** & **npm**

### 2. Backend Setup
```bash
# Navigate to project root
cd CitizenRights

# Install Python dependencies
pip install fastapi uvicorn pydantic python-dotenv

# Start the FastAPI backend
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```
The API server starts at `http://127.0.0.1:8000`. Swagger API documentation is available at `http://127.0.0.1:8000/docs`.

### 3. Frontend Setup
```bash
# In a separate terminal, navigate to frontend directory
cd frontend

# Install npm dependencies
npm install

# Start development server
npm run dev
```
Open `http://localhost:5173` in your browser.

---

## Educational Disclaimer

> **Important Public Notice**: NyaayaAI provides general informational and educational content on Indian laws, constitutional protections, and administrative procedures. It is **not** a substitute for certified legal counsel or official government notifications. Laws and departmental procedures are subject to statutory amendments. Always verify important matters with official Government Gazettes, department portals, or practicing advocates.
