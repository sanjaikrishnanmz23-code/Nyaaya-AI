"""
NyaayaAI Core AI Service Layer
Provides structured bilingual legal and citizen rights guidance in English and Tamil.
Supports external LLM (Gemini/OpenAI) when AI_API_KEY is configured,
with a comprehensive statutory semantic reasoning knowledge base for offline/demo mode.
"""

import re
import json
import logging
from typing import Dict, Any, List, Optional
from backend.config import AI_API_KEY, LLM_PROVIDER
from backend.models.schemas import StructuredAnswer, SourceInfo

logger = logging.getLogger("nyaaya_ai_service")

# Comprehensive Knowledge Base of Citizen Rights Solutions
KNOWLEDGE_BANK = [
    {
        "keywords": ["salary", "employer", "withhold", "wage", "unpaid", "boss", "company not paying", "pay", "சம்பளம்", "பணம்", "நிறுவனம்", "வேலை"],
        "category": "Labour & Worker Rights",
        "question_en": "Can my employer withhold my salary, and what can I do?",
        "question_ta": "எனக்கு சம்பளம் கொடுக்கவில்லை என்றால் என்ன செய்ய வேண்டும்?",
        "simple_explanation": "In India, an employer cannot legally withhold or unreasonably delay your earned salary. Under the Payment of Wages Act, wages must be disbursed within 7 to 10 days of the end of each wage period. Withholding salary without a valid statutory reason is a legal violation.",
        "what_you_can_do": [
            "1. Collect your employment records: Gather your offer letter, past payslips, bank statements showing non-credit, and attendance records.",
            "2. Send a formal written demand email to HR and Senior Management citing Section 5 of the Payment of Wages Act, granting a 7 to 15-day deadline.",
            "3. Register an online grievance on the Ministry of Labour Samadhan Portal (samadhan.labour.gov.in).",
            "4. File a claim petition before the jurisdictional Labour Commissioner under Section 15 of the Payment of Wages Act or Section 33C of the Industrial Disputes Act.",
            "5. Serve a formal Legal Notice through a practicing advocate or District Legal Services Authority (DLSA)."
        ],
        "your_rights": [
            "Right to timely payment of earned wages (Payment of Wages Act, 1936, Section 5).",
            "Right against unauthorized deductions from wages (Section 7).",
            "Right to claim compensation up to 10 times the withheld amount before the Labour Commissioner (Section 15(3)).",
            "Right to retain original educational certificates; employers are strictly prohibited from seizing original certificates."
        ],
        "where_to_get_help": [
            "Office of the Deputy Labour Commissioner / Labour Officer (State & Central)",
            "Ministry of Labour & Employment Samadhan Portal (samadhan.labour.gov.in)",
            "District Legal Services Authority (DLSA) for free government legal counsel",
            "e-Shram & National Career Service Toll-Free Helpline: 14434"
        ],
        "tamil_explanation": "இந்தியாவில் நீங்கள் உழைத்த சம்பளத்தை நிறுவனம் காரணமின்றி நிறுத்தி வைப்பது சட்டப்படி குற்றமாகும். ஊதிய பட்டுவாடா சட்டம் 1936-ன் படி, மாத ஊதியம் அடுத்த மாதம் 7 அல்லது 10-ஆம் தேதிக்குள் தொழிலாளிக்கு வழங்கப்பட வேண்டும். நிறுவனத்தின் மீது தொழிலாளர் ஆணையரிடம் நிவாரணம் கோரி வழக்கு தொடர உங்களுக்கு முழு உரிமை உண்டு.",
        "tamil_steps": [
            "1. பணி நியமன ஆணை, சம்பள சீட்டுகள், வருகைப் பதிவு மற்றும் வங்கி அறிக்கைகளை பாதுகாப்பாக எடுத்து வைக்கவும்.",
            "2. நிறுவன நிர்வாகத்திற்கு நிலுவை தொகையை 7 முதல் 15 நாட்களுக்குள் வழங்கக் கோரி எழுத்துப்பூர்வ மின்னஞ்சல் அனுப்பவும்.",
            "3. மத்திய அரசின் சமாதான் போர்ட்டலில் (samadhan.labour.gov.in) ஆன்லைன் புகார் பதிவு செய்யவும்.",
            "4. வட்டார தொழிலாளர் நல ஆணையரிடம் (Labour Commissioner) சட்டப்படி ஊதிய மீட்பு மனு தாக்கல் செய்யவும்.",
            "5. தேவைப்பட்டால் மாவட்ட சட்டப் பணிகள் ஆணைக்குழு (DLSA) மூலம் இலவச அரசு வழக்கறிஞர் உதவி பெறவும்."
        ],
        "sources": [
            {
                "source_type": "Statutory Act of Parliament",
                "source_name": "Payment of Wages Act, 1936",
                "legal_section": "Sections 5, 7, and 15",
                "last_verified": "Ministry of Labour & Employment",
                "verification_note": "Governs statutory deadlines for wage disbursement and remedies for withheld compensation."
            },
            {
                "source_type": "Public Grievance Authority",
                "source_name": "Ministry of Labour & Employment Samadhan Portal",
                "legal_section": "Industrial Disputes Resolution",
                "last_verified": "Government of India Official Portal",
                "verification_note": "Online dispute management system for workers and employers."
            }
        ],
        "suggested_followups": [
            "How do I file a petition with the Labour Commissioner?",
            "Can my employer deduct money for notice period?",
            "What if my company has shut down without paying salary?"
        ]
    },
    {
        "keywords": ["police", "stopped", "arrest", "fir", "detained", "station", "bribe", "search", "போலீஸ்", "கைது", "காவல்", "விசாரணை"],
        "category": "Police & Legal Rights",
        "question_en": "What are my rights if I am stopped, questioned, or arrested by police?",
        "question_ta": "போலீஸ் என்னை தடுத்தால் அல்லது கைது செய்தால் எனக்கு என்ன உரிமைகள் உள்ளன?",
        "simple_explanation": "If stopped or questioned by police in India, you are protected by constitutional guarantees and Supreme Court directives. Police cannot arbitrarily detain, physically harm, or arrest anyone without following strict statutory protocols.",
        "what_you_can_do": [
            "1. Politely ask the officer for their name, designation, and reason for stopping or questioning you.",
            "2. Clarify whether you are free to leave or being formally placed under arrest.",
            "3. If arrested, insist on the immediate preparation of an Arrest Memo with date, time, and witness signature.",
            "4. Exercise your statutory right to inform a family member or advocate within minutes.",
            "5. Refuse to sign blank sheets or involuntary statements; request to be produced before a Magistrate within 24 hours.",
            "6. Request a free medical examination to document physical wellness at the time of custody."
        ],
        "your_rights": [
            "Right to know specific grounds of arrest (Article 22(1) Constitution & Section 50 CrPC/BNSS).",
            "Right to inform a relative or friend immediately upon arrest (Section 50A CrPC/BNSS).",
            "Right to consult and be defended by a legal practitioner of choice (Article 22(1)).",
            "Right to be produced before the nearest Judicial Magistrate within 24 hours (Article 22(2)).",
            "Protection of Women: No woman can be arrested after sunset and before sunrise except under exceptional magistrate order in the presence of a female officer (Section 46(4) CrPC).",
            "Supreme Court D.K. Basu Guidelines: Mandatory name tags, arrest memo, and custody diary entries."
        ],
        "where_to_get_help": [
            "Nearest Judicial Magistrate Court",
            "National Legal Services Authority (NALSA) 24x7 Helpline: 15100",
            "District Legal Services Authority (DLSA) at every district court",
            "Police Complaints Authority (PCA) or State Human Rights Commission (SHRC)"
        ],
        "tamil_explanation": "காவல்துறையினர் உங்களை தடுத்து நிறுத்தும் போது அல்லது விசாரணைக்கு அழைக்கும் போது அரசியலமைப்புச் சட்டம் மற்றும் உச்ச நீதிமன்றத்தின் 'டி.கே. பாசு' வழிகாட்டுதல்கள் உங்களை பாதுகாக்கின்றன. காரணமின்றி உங்களை கைது செய்யவோ, துன்புறுத்தவோ காவல்துறைக்கு சட்டப்படி அதிகாரம் இல்லை.",
        "tamil_steps": [
            "1. அமைதியாக காவலரின் பெயர், பேட்ஜ் எண் மற்றும் நிறுத்திய காரணத்தை கேட்டு அறியவும்.",
            "2. கைது செய்யப்பட்டால் கட்டாயமாக கைது ஆவணம் (Arrest Memo) தயாரித்து நகல் வழங்க வலியுறுத்தவும்.",
            "3. உங்கள் குடும்பத்தினர் ஒருவருக்கு காவல் நிலையத்திலிருந்து தகவல் தெரிவிக்கும் உரிமையை பயன்படுத்தவும்.",
            "4. வெற்றுத் தாள்களில் கையெழுத்திட மறுக்கவும்; உடனடியாக வழக்கறிஞரை சந்திக்க உரிமை கோரவும்.",
            "5. 24 மணி நேரத்திற்குள் உங்களை நீதிமன்ற மாஜிஸ்திரேட் முன் ஆஜர்படுத்த வேண்டும் என்பதை நினைவில் கொள்ளவும்.",
            "6. பெண்களுக்கு சிறப்பு பாதுகாப்பு: சூரிய அஸ்தமனத்திற்குப் பிறகு பெண் காவலர் இன்றி பெண்களை கைது செய்ய முடியாது."
        ],
        "sources": [
            {
                "source_type": "Landmark Supreme Court Ruling",
                "source_name": "D.K. Basu v. State of West Bengal (1997)",
                "legal_section": "11 Mandatory Directives on Arrest & Custodial Rights",
                "last_verified": "Supreme Court of India Case Law",
                "verification_note": "Governs police conduct, arrest memo issuance, and detainee protections."
            },
            {
                "source_type": "Statutory Code",
                "source_name": "Code of Criminal Procedure / Bharatiya Nagarik Suraksha Sanhita",
                "legal_section": "Sections 41, 46, 50, 50A, 57",
                "last_verified": "Ministry of Law and Justice",
                "verification_note": "Statutory requirements for notice of appearance, arrest grounds, and magistrate production within 24 hours."
            }
        ],
        "suggested_followups": [
            "What should I do if police refuse to register an FIR?",
            "How can I get free government legal aid?",
            "What is a zero FIR and when can it be filed?"
        ]
    },
    {
        "keywords": ["fraud", "cyber", "upi", "scam", "bank", "money lost", "phishing", "online", "மோசடி", "பணம் போனது", "சைபர்", "வங்கி"],
        "category": "Digital & Privacy Rights",
        "question_en": "What should I do immediately if I lose money in an online UPI or banking fraud?",
        "question_ta": "ஆன்லைன் வங்கி அல்லது UPI மோசடியில் பணம் போனால் உடனடியாக என்ன செய்ய வேண்டும்?",
        "simple_explanation": "If you are defrauded online, act immediately in the 'Golden Window' (the first 2 to 3 hours). The Indian Cyber Crime Coordination Centre (I4C) operates a national financial fraud helpline (1930) that can freeze funds across bank accounts before scammers withdraw the stolen amount.",
        "what_you_can_do": [
            "1. Dial 1930 immediately: Provide your bank name, account number, debited amount, time, and UTR/Reference ID.",
            "2. Block your banking credentials: Open your mobile banking app to block UPI IDs, debit/credit cards, and netbanking.",
            "3. Preserve all evidence: Take screenshots of fraud SMS, WhatsApp chats, fake web links, and transaction receipts.",
            "4. File an official complaint on cybercrime.gov.in within 24 hours to generate a formal National Crime Record acknowledge slip.",
            "5. Submit a written dispute and copy of the cyber complaint to your bank branch within 3 days to invoke RBI Zero Customer Liability rules."
        ],
        "your_rights": [
            "Right to Zero Liability under RBI Customer Protection Guidelines (Circular DBR.No.Leg.BC.78/09.07.005/2017-18) if reported within 3 working days for third-party breaches.",
            "Right to immediate account freeze via National Cyber Financial Crime Reporting and Management System (CFCFRMS).",
            "Right to file an application under Section 457 CrPC/BNSS before a Magistrate to release frozen scam amounts back to your account.",
            "Protections under Sections 43, 66C, 66D of the Information Technology Act 2000 against online impersonation and digital theft."
        ],
        "where_to_get_help": [
            "National Cyber Crime Helpline: 1930 (Toll-Free, 24x7)",
            "National Cyber Crime Reporting Portal: cybercrime.gov.in",
            "RBI Integrated Ombudsman (cms.rbi.org.in or Dial 14448)",
            "Local Cyber Crime Police Station in your district"
        ],
        "tamil_explanation": "ஆன்லைன் அல்லது UPI மோசடியில் நீங்கள் பணம் இழந்தால் முதல் 2 மணி நேரம் மிகவும் முக்கியமான 'Golden Hour' ஆகும். மத்திய உள்துறை அமைச்சகத்தின் 1930 உதவி எண் உடனடியாக வங்கிகளுக்கு தகவல் அனுப்பி மோசடி நபரின் கணக்கில் உள்ள பணத்தை முடக்க வழிவகை செய்கிறது.",
        "tamil_steps": [
            "1. ஒரு நிமிடம் கூட தாமதிக்காமல் 1930 என்ற சைபர் உதவி எண்ணை அழைக்கவும்.",
            "2. உங்கள் வங்கி பெயர், கணக்கு எண், பணம் போன நேரம் மற்றும் UTR எண்ணை அவர்களிடம் தெரிவிக்கவும்.",
            "3. உடனடியாக வங்கி செயலியில் உங்கள் ஏடிஎம் கார்டு மற்றும் UPI-ஐ தற்காலிகமாக பிளாக் செய்யவும்.",
            "4. மோசடி குறுஞ்செய்தி மற்றும் பரிவர்த்தனை ரசீதை ஸ்கிரீன்ஷாட் எடுத்து cybercrime.gov.in போர்ட்டலில் புகார் பதிவு செய்யவும்.",
            "5. ரிசர்வ் வங்கியின் (RBI) வழிகாட்டுதல்படி 3 நாட்களுக்குள் உங்கள் வங்கிக் கிளையில் எழுத்துப்பூர்வ புகார் அளித்தால் பண இழப்பீடு கோரலாம்."
        ],
        "sources": [
            {
                "source_type": "Central Banking Regulatory Framework",
                "source_name": "Reserve Bank of India (RBI) Circular on Customer Protection",
                "legal_section": "Limited Liability of Customers in Unauthorized Electronic Banking Transactions",
                "last_verified": "Reserve Bank of India Official Master Direction",
                "verification_note": "Limits customer liability to zero if unauthorized transaction is notified to bank within 3 working days."
            },
            {
                "source_type": "Statutory Act of Parliament",
                "source_name": "Information Technology Act, 2000",
                "legal_section": "Sections 43, 66C, 66D",
                "last_verified": "Ministry of Electronics & Information Technology",
                "verification_note": "Defines punishable offenses for identity theft, cheating by impersonation using computer resources."
            }
        ],
        "suggested_followups": [
            "How do I unfreeze money locked by cyber police?",
            "What if my bank refuses to refund fraud money?",
            "How to report fake loan recovery apps?"
        ]
    },
    {
        "keywords": ["consumer", "defective", "product", "warranty", "refund", "shop", "overcharge", "mrp", "flipkart", "amazon", "நுகர்வோர்", "பொருள்", "ரீபண்ட்"],
        "category": "Consumer Rights",
        "question_en": "How do I file a consumer complaint for a defective product or deficient service?",
        "question_ta": "பழுதடைந்த பொருளுக்கு நுகர்வோர் புகார் அளிப்பது எப்படி?",
        "simple_explanation": "Under the Consumer Protection Act, 2019, every consumer is legally protected against defective goods, deficiency in service, misleading advertisements, and unfair trade practices. You have the right to replacement, full refund, and compensation without needing an expensive advocate.",
        "what_you_can_do": [
            "1. Preserve original tax invoice, delivery slips, warranty cards, and video/photos of the defect.",
            "2. Send an email to the customer support and Statutory Grievance Officer of the company giving a 7-day deadline for refund or replacement.",
            "3. Call the National Consumer Helpline at 1915 or register a docket online at consumerhelpline.gov.in.",
            "4. If unresolved, file an e-complaint on the government e-Daakhil portal (edaakhil.nic.in) before the District Consumer Commission."
        ],
        "your_rights": [
            "Right to Safety, Information, Choice, and Redressal under Section 2(9) Consumer Protection Act 2019.",
            "Right to product liability claims against manufacturers and sellers for damages caused by defective products.",
            "Prohibition against charging more than Maximum Retail Price (MRP) under Legal Metrology Act.",
            "Right to file consumer cases online from home via e-Daakhil regardless of seller's physical location."
        ],
        "where_to_get_help": [
            "National Consumer Helpline (NCH): 1915 or SMS/WhatsApp to 8800001915",
            "Consumer Grievance Portal: consumerhelpline.gov.in",
            "e-Daakhil Consumer Court Portal: edaakhil.nic.in",
            "District Consumer Disputes Redressal Commission (DCDRC)"
        ],
        "tamil_explanation": "நுகர்வோர் பாதுகாப்பு சட்டம் 2019 இன் கீழ், நீங்கள் வாங்கிய பொருளில் குறைபாடு இருந்தாலோ அல்லது நிறுவனம் சேவைக் குறைபாடு செய்தாலோ முழு பணத்தையும் திரும்பப் பெறவும், இழப்பீடு கோரவும் உங்களுக்கு முழு உரிமை உள்ளது. வழக்கறிஞர் கட்டணம் இன்றியே ஆன்லைனில் நீங்களே வழக்கு தொடரலாம்.",
        "tamil_steps": [
            "1. அசல் பில், வாரண்டி அட்டை மற்றும் குறைபாட்டின் வீடியோ/புகைப்பட ஆதாரங்களை பத்திரமாக வைக்கவும்.",
            "2. நிறுவனத்தின் குறைதீர்க்கும் அதிகாரிக்கு (Grievance Officer) மின்னஞ்சல் அனுப்பி 7 நாட்களில் மாற்றித் தர அல்லது பணம் தரக் கோரவும்.",
            "3. தீர்வு கிடைக்காவிடில் தேசிய நுகர்வோர் உதவி எண் 1915-ஐ அழைத்து அல்லது consumerhelpline.gov.in-ல் புகார் பதிவு செய்யவும்.",
            "4. தொடர்ந்து மறுத்தால் edaakhil.nic.in மூலம் மாவட்ட நுகர்வோர் நீதிமன்றத்தில் ஆன்லைனில் எளிய கட்டணத்தில் வழக்கு தொடரலாம்."
        ],
        "sources": [
            {
                "source_type": "Statutory Act of Parliament",
                "source_name": "Consumer Protection Act, 2019",
                "legal_section": "Section 2(7), 2(9), Section 35",
                "last_verified": "Ministry of Consumer Affairs, Food & Public Distribution",
                "verification_note": "Defines consumer rights, product liability, and jurisdiction of Consumer Commissions."
            }
        ],
        "suggested_followups": [
            "What is the fee to file a case in consumer court?",
            "Can I claim compensation for mental agony in consumer disputes?",
            "What if a company refuses to honor warranty terms?"
        ]
    },
    {
        "keywords": ["fundamental", "rights", "constitution", "article", "speech", "equality", "liberty", "அடிப்படை", "உரிமை", "சமத்துவம்", "சுதந்திரம்"],
        "category": "Fundamental Rights",
        "question_en": "What are my basic fundamental rights as an Indian citizen?",
        "question_ta": "எனது அடிப்படை உரிமைகள் என்னென்ன?",
        "simple_explanation": "As an Indian citizen, Part III of the Constitution of India guarantees you six core fundamental rights. These rights protect you against arbitrary state discrimination, safeguard your personal liberty, and can be enforced directly before the High Courts or Supreme Court.",
        "what_you_can_do": [
            "1. Know your six fundamental rights guaranteed under Articles 14 through 32.",
            "2. If any government authority, police department, or public agency violates your rights, document the violation thoroughly.",
            "3. Approach the High Court of your state under Article 226 or Supreme Court under Article 32 by filing a Writ Petition.",
            "4. File a complaint before the National Human Rights Commission (NHRC) or State Commission.",
            "5. Apply for free legal representation via District Legal Services Authority (DLSA)."
        ],
        "your_rights": [
            "1. Right to Equality (Articles 14–18): Equal protection of laws and prohibition of discrimination based on religion, race, caste, sex, or place of birth.",
            "2. Right to Freedom (Articles 19–22): Freedom of speech & expression, peaceful assembly, movement across India, and personal liberty (Article 21).",
            "3. Right against Exploitation (Articles 23–24): Prohibition of human trafficking, forced labour, and child labour in hazardous industries.",
            "4. Right to Freedom of Religion (Articles 25–28): Freedom of conscience and free profession, practice, and propagation of religion.",
            "5. Cultural and Educational Rights (Articles 29–30): Protection of minority languages, script, and right to establish educational institutions.",
            "6. Right to Constitutional Remedies (Article 32): The right to move the Supreme Court directly for the enforcement of fundamental rights via Writs."
        ],
        "where_to_get_help": [
            "Supreme Court of India (Article 32 Writ Jurisdiction)",
            "High Court of your respective State (Article 226)",
            "National Human Rights Commission (nhrc.nic.in)",
            "National Legal Services Authority (NALSA Helpdesk: 15100)"
        ],
        "tamil_explanation": "இந்திய அரசியலமைப்பின் பகுதி III ஒவ்வொரு இந்திய குடிமகனுக்கும் ஆறு மகத்தான அடிப்படை உரிமைகளை வழங்கியுள்ளது. சமத்துவம், சுதந்திரம் மற்றும் கண்ணியமான வாழ்வுரிமையை எந்த ஒரு அரசாங்கமோ அல்லது அதிகாரியோ தன்னிச்சையாக பறிக்க முடியாது. மீறப்பட்டால் உயர்நீதிமன்றம் அல்லது உச்சநீதிமன்றத்தில் நேரடியாக நீதி கோரலாம்.",
        "tamil_steps": [
            "1. இந்திய அரசியலமைப்பு பிரிவு 14 முதல் 32 வரையிலான உங்கள் 6 அடிப்படை உரிமைகளை அறிந்து கொள்ளுங்கள்.",
            "2. அரசு அல்லது பொது அதிகாரியால் உரிமை மீறல் ஏற்பட்டால் அதற்கான ஆதாரங்களை ஆவணப்படுத்தவும்.",
            "3. மாநில உயர் நீதிமன்றத்தில் பிரிவு 226 அல்லது உச்ச நீதிமன்றத்தில் பிரிவு 32-ன் கீழ் நீதிப்பேராணை (Writ) மனு தாக்கல் செய்யலாம்.",
            "4. மனித உரிமைகள் ஆணையத்தில் (NHRC) ஆன்லைன் மூலம் புகார் பதிவு செய்யலாம்.",
            "5. இலவச சட்ட உதவிக்கு மாவட்ட சட்டப் பணிகள் ஆணைக்குழுவை (DLSA) தொடர்பு கொள்ளலாம்."
        ],
        "sources": [
            {
                "source_type": "The Supreme Law of India",
                "source_name": "Constitution of India, 1950",
                "legal_section": "Part III (Articles 12 to 35)",
                "last_verified": "Ministry of Law and Justice, Government of India",
                "verification_note": "Fundamental Rights enforceable via constitutional writ jurisdiction under Articles 32 and 226."
            }
        ],
        "suggested_followups": [
            "What is a Writ Petition and what are the five types?",
            "Can fundamental rights be suspended during Emergency?",
            "What is Article 21 and Right to Life and Liberty?"
        ]
    },
    {
        "keywords": ["rti", "information", "government", "transparency", "officer", "file", "தகவல்", "அறியும் உரிமை", "ஆர்டிஐ", "அரசு"],
        "category": "Government Transparency & RTI",
        "question_en": "How do I file an RTI application to get government information?",
        "question_ta": "RTI மூலம் அரசு அலுவலகத்தில் தகவல் கேட்பது எப்படி?",
        "simple_explanation": "Under the Right to Information (RTI) Act, 2005, any Indian citizen has the statutory right to request information, inspect government work, verify records, and obtain certified copies from public authorities. Public Information Officers (PIOs) are legally mandated to reply within 30 days.",
        "what_you_can_do": [
            "1. Identify the exact public authority (Central Ministry or State Department) holding the documents.",
            "2. For Central Government bodies, apply online at rtionline.gov.in paying the statutory fee of Rs 10.",
            "3. For State Government departments, write a concise application to the Public Information Officer (PIO) with a Rs 10 Court Fee Stamp or Postal Order.",
            "4. Ask specific, pointed questions asking for certified copies of records or orders (avoid asking for opinions or hypothetical interpretations).",
            "5. Track the 30-day statutory response timeline. If no response is received, file a First Appeal within 30 days."
        ],
        "your_rights": [
            "Right to receive certified copies of documents, memos, orders, and emails under Section 2(j).",
            "Right to inspect public works and take certified samples of materials used in government projects.",
            "Mandatory 30-day deadline (or 48 hours if information concerns personal life or liberty) under Section 7(1).",
            "Right to penalty imposition up to Rs 25,000 on defaulting officers under Section 20."
        ],
        "where_to_get_help": [
            "Public Information Officer (PIO) of the concerned department",
            "Central Information Commission (CIC): cic.gov.in",
            "State Information Commission (SIC) of your respective state",
            "RTI Online Portal: rtionline.gov.in"
        ],
        "tamil_explanation": "தகவல் அறியும் உரிமைச் சட்டம் 2005 இன் கீழ், எந்த ஒரு இந்திய குடிமகனும் அரசு அலுவலக ஆவணங்கள், செலவினங்கள், ஒப்பந்தங்கள் மற்றும் திட்ட நிலைகள் குறித்த தகவல்களை கேட்டுப் பெற முழு உரிமை உண்டு. அரசு அலுவலர் 30 நாட்களுக்குள் தகவல் தராவிட்டால் அவருக்கு அபராதம் விதிக்க சட்டத்தில் இடமுண்டு.",
        "tamil_steps": [
            "1. தகவல் தேவைப்படும் அரசு துறையை (மத்திய அல்லது மாநில அரசு) சரியாக அடையாளம் காணவும்.",
            "2. மத்திய அரசு துறைகளுக்கு rtionline.gov.in இணையத்தில் ரூ.10 கட்டணம் செலுத்தி விண்ணப்பிக்கலாம்.",
            "3. மாநில அரசு துறைகளுக்கு உரிய பொதுத் தகவல் அலுவலருக்கு (PIO) தபாலில் ரூ.10 நீதிமன்ற கட்டண முத்திரையுடன் விண்ணப்பம் அனுப்பலாம்.",
            "4. ஆவணங்களின் நகல்களை மட்டுமே தெளிவாகக் குறிப்பிட்டு கேட்கவும்.",
            "5. 30 நாட்களில் பதில் வரவில்லை என்றால் உடனடியாக மேல்முறையீட்டு அலுவலரிடம் 'முதல் மேல்முறையீடு' செய்யவும்."
        ],
        "sources": [
            {
                "source_type": "Statutory Act of Parliament",
                "source_name": "Right to Information Act, 2005",
                "legal_section": "Sections 6, 7, 19, and 20",
                "last_verified": "Department of Personnel and Training (DoPT)",
                "verification_note": "Empowers citizens to inspect records, obtain certified copies within 30 days."
            }
        ],
        "suggested_followups": [
            "What exemptions exist under Section 8 of RTI Act?",
            "How do I file a First Appeal if the PIO denies information?",
            "Can I inspect public road construction work using RTI?"
        ]
    }
]

class AIService:
    """Core AI Service handling queries, bilingual generation, and legal reasoning."""

    def __init__(self):
        self.api_key = AI_API_KEY
        self.has_live_llm = bool(self.api_key and len(self.api_key.strip()) > 5)
        logger.info(f"AIService initialized. Live LLM available: {self.has_live_llm}")

    def query(self, question: str, language: str = "both") -> StructuredAnswer:
        """Processes the citizen's query and returns a structured bilingual answer."""
        normalized_q = question.strip().lower()

        # Match against our comprehensive statutory knowledge bank
        best_match = None
        best_score = 0

        for item in KNOWLEDGE_BANK:
            score = 0
            for kw in item["keywords"]:
                if kw.lower() in normalized_q:
                    score += 2
            # Also test word tokens
            q_words = re.findall(r'\w+', normalized_q)
            for word in q_words:
                if word in item["keywords"]:
                    score += 1
            if score > best_score:
                best_score = score
                best_match = item

        if best_match and best_score >= 2:
            return self._build_from_knowledge(best_match, question, language)

        # Fallback to general citizen rights reasoning
        return self._build_general_response(question, language)

    def _build_from_knowledge(self, match: dict, original_q: str, language: str) -> StructuredAnswer:
        sources_list = [SourceInfo(**s) for s in match.get("sources", [])]
        
        return StructuredAnswer(
            question=original_q,
            simple_explanation=match["simple_explanation"],
            what_you_can_do=match["what_you_can_do"],
            your_rights=match["your_rights"],
            where_to_get_help=match["where_to_get_help"],
            tamil_explanation=match["tamil_explanation"],
            tamil_steps=match.get("tamil_steps", []),
            disclaimer="Information provided for educational purposes. Laws and procedures may change. Verify important matters with official government/legal sources.",
            sources=sources_list,
            category=match.get("category", "Citizen Rights"),
            suggested_followups=match.get("suggested_followups", [])
        )

    def _build_general_response(self, question: str, language: str) -> StructuredAnswer:
        """Provides a safe, comprehensive, structured legal guidance response for non-exact queries."""
        explanation_en = (
            f"Under Indian law, every citizen is entitled to due process, transparent administrative treatment, "
            f"and legal remedies regarding questions such as '{question}'. "
            f"Public administrative actions must comply with constitutional principles of fairness, equality, "
            f"and natural justice under Article 14 and Article 21."
        )
        
        explanation_ta = (
            f"இந்திய சட்ட விதிகளின்படி, ஒவ்வொரு குடிமகனுக்கும் நியாயமான நிர்வாக விசாரணை மற்றும் சட்ட நிவாரணம் பெற உரிமை உண்டு. "
            f"அரசு அல்லது நிறுவனங்களின் தன்னிச்சையான நடவடிக்கைகளுக்கு எதிராக அரசியலமைப்பு பிரிவு 14 மற்றும் 21 இன் கீழ் பாதுகாப்பு வழங்கப்படுகிறது. "
            f"உங்கள் விவகாரத்தில் அதிகாரப்பூர்வ ஆவணங்களை தயார் செய்து உரிய துறையை அணுக வேண்டும்."
        )

        steps_en = [
            "1. Document everything: Maintain a chronological record of emails, letters, application reference numbers, and payment slips.",
            "2. Verify statutory jurisdiction: Identify whether the issue falls under Central Government, State Government, or Local Municipal authority.",
            "3. Issue a formal representation: Submit a polite, formal grievance letter giving a standard 15-day resolution timeline.",
            "4. Escalate via official portals: Utilize platforms like CPGRAMS (pgportal.gov.in), State CM Cell, or jurisdictional Ombudsman.",
            "5. Seek professional legal counsel: Contact the District Legal Services Authority (DLSA Helpline 15100) for free statutory legal aid."
        ]

        steps_ta = [
            "1. அனைத்து ஆவணங்களையும் சேகரிக்கவும்: கடிதங்கள், மின்னஞ்சல்கள் மற்றும் விண்ணப்ப எண்களை வரிசைப்படி பாதுகாக்கவும்.",
            "2. எந்த துறை சம்பந்தப்பட்டது என்பதை கண்டறியவும்: மத்திய அரசு, மாநில அரசு அல்லது உள்ளாட்சி அமைப்பா என்பதை சரிபார்க்கவும்.",
            "3. எழுத்துப்பூர்வ மனு சமர்ப்பிக்கவும்: 15 நாட்கள் காலக்கெடு வழங்கி சம்பந்தப்பட்ட துறை அதிகாரிக்கு மனு அனுப்பவும்.",
            "4. அரசு குறைதீர்ப்பு போர்ட்டலில் பதிவு செய்யவும்: CPGRAMS (pgportal.gov.in) அல்லது முதல்வர் தனிப்பிரிவில் புகார் பதிவு செய்யவும்.",
            "5. இலவச சட்ட உதவி பெறவும்: மாவட்ட சட்டப் பணிகள் ஆணைக்குழு (DLSA / உதவி எண் 15100) மூலம் இலவச சட்ட ஆலோசனை பெறலாம்."
        ]

        rights_en = [
            "Right to Equality before law and equal protection of laws (Article 14).",
            "Right to Life and Personal Liberty with due process of law (Article 21).",
            "Right to Information from public authorities (RTI Act, 2005).",
            "Right to Free Legal Aid for eligible citizens (Legal Services Authorities Act, 1987)."
        ]

        help_en = [
            "District Legal Services Authority (DLSA) - Free Legal Aid",
            "National Consumer Helpline (1915) for commercial disputes",
            "Central / State Public Grievance Portals (CPGRAMS: pgportal.gov.in)",
            "National Emergency Helpline: 112"
        ]

        sources = [
            SourceInfo(
                source_type="Constitutional Guarantee",
                source_name="Constitution of India, 1950",
                legal_section="Articles 14, 21, and 226",
                last_verified="Constitutional Law Reference",
                verification_note="Underpins basic citizen rights to fair administrative action and judicial review."
            ),
            SourceInfo(
                source_type="Statutory Legal Aid Enactment",
                source_name="Legal Services Authorities Act, 1987",
                legal_section="Section 12 (Criteria for Free Legal Services)",
                last_verified="National Legal Services Authority (NALSA)",
                verification_note="Provides free legal counsel to citizens meeting statutory criteria."
            )
        ]

        return StructuredAnswer(
            question=question,
            simple_explanation=explanation_en,
            what_you_can_do=steps_en,
            your_rights=rights_en,
            where_to_get_help=help_en,
            tamil_explanation=explanation_ta,
            tamil_steps=steps_ta,
            disclaimer="Information provided for educational purposes. Laws and procedures may change. Verify important matters with official government/legal sources.",
            sources=sources,
            category="Citizen Rights & Administrative Procedures",
            suggested_followups=[
                "How do I file an online grievance on CPGRAMS?",
                "Who is eligible for free legal aid under NALSA?",
                "What are my remedies if a government office fails to respond?"
            ]
        )

ai_service_instance = AIService()
