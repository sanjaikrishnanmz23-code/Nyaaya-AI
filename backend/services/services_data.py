"""
Government Services Directory Database
Essential Indian public services with bilingual documentation, eligibility, steps, and verified official portals.
"""

GOVERNMENT_SERVICES = [
    {
        "id": "aadhaar-services",
        "title": "Aadhaar Card Services",
        "title_tamil": "ஆதார் அட்டை சேவைகள்",
        "category": "Identity & Documentation",
        "icon": "Fingerprint",
        "description": "Enrollment for new 12-digit unique identity, biometric updates, address changes, mobile number linking, and biometric lock.",
        "description_tamil": "புதிய ஆதார் பதிவு, கைரேகை/கருவிழி புதுப்பித்தல், முகவரி மாற்றம், மொபைல் எண் இணைப்பு மற்றும் பயோமெட்ரிக் லாக் வசதி.",
        "eligibility": [
            "Every resident of India residing for 182 days or more in the preceding 12 months.",
            "Newborn children can be enrolled using birth certificate (Baal Aadhaar)."
        ],
        "required_documents": [
            "Proof of Identity (POI): Passport, PAN card, Ration card, Voter ID, Driving Licence.",
            "Proof of Address (POA): Electricity bill, Water bill, Bank Passbook, Rent Agreement.",
            "Proof of Date of Birth (DOB): Birth certificate, SSLC/10th marksheet.",
            "Proof of Relationship (POR) for child enrollment."
        ],
        "step_by_step_process": [
            "Visit the official UIDAI portal (myaadhaar.uidai.gov.in) to book an appointment or update address online.",
            "For demographic updates (address), upload self-attested supporting document.",
            "For mobile number or biometric updates (fingerprint/photo), visit nearest Aadhaar Seva Kendra.",
            "Track update status using 28-digit Service Request Number (SRN) or Enrollment ID (EID).",
            "Download updated e-Aadhaar PDF using registered mobile OTP."
        ],
        "relevant_authority": "Unique Identification Authority of India (UIDAI), Ministry of Electronics & IT",
        "official_portal_name": "MyAadhaar UIDAI Portal",
        "official_url_demo": "https://myaadhaar.uidai.gov.in",
        "processing_time": "15 to 30 days for updates; Instant e-Aadhaar download once approved.",
        "fee_structure": "Free for first enrollment & mandatory biometric update (age 5 & 15); Rs 50 for demographic, Rs 100 for biometric updates."
    },
    {
        "id": "pan-card-services",
        "title": "PAN Card (Permanent Account Number)",
        "title_tamil": "பான் கார்டு சேவைகள் (PAN)",
        "category": "Tax & Financial Identity",
        "icon": "CreditCard",
        "description": "Issuance of 10-character alphanumeric tax identifier, correction of names/birthdates, duplicate card requests, and Aadhaar-PAN linkage.",
        "description_tamil": "10 இலக்க வருமான வரி அடையாள அட்டை, பெயர்/பிறந்த தேதி திருத்தம், நகல் அட்டை பெறுதல் மற்றும் ஆதார்-பான் இணைப்பு.",
        "eligibility": [
            "Any Indian citizen, NRI, company, firm, or minor through natural guardian who undertakes financial transactions."
        ],
        "required_documents": [
            "Proof of Identity: Aadhaar Card, Voter ID, Passport, Driving Licence.",
            "Proof of Address: Aadhaar Card, Bank statement, Utility bill.",
            "Proof of Date of Birth: Birth certificate, Matriculation certificate, Passport."
        ],
        "step_by_step_process": [
            "Apply via Protean (formerly NSDL) or UTIITSL official online portal.",
            "Choose Form 49A for Indian citizens or Form 49AA for foreign citizens.",
            "Authenticate digitally using Aadhaar e-KYC (paperless instant e-PAN available).",
            "Pay the prescribed statutory processing fee online.",
            "Physical card is delivered by India Post to the applicant's address; instant e-PAN generated in minutes."
        ],
        "relevant_authority": "Income Tax Department, Ministry of Finance, Government of India",
        "official_portal_name": "Protean (NSDL) / UTIITSL PAN Portal",
        "official_url_demo": "https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html",
        "processing_time": "Instant for paperless e-PAN; 10 to 15 days for physical plastic card delivery.",
        "fee_structure": "Approx Rs 107 for physical delivery within India; Rs 1,017 for overseas addresses."
    },
    {
        "id": "passport-seva",
        "title": "Passport Seva",
        "title_tamil": "பாஸ்போர்ட் சேவா (கடவுச்சீட்டு)",
        "category": "Travel & Citizenship",
        "icon": "Compass",
        "description": "Online application for fresh Indian passport, renewal/reissue, Tatkaal expedited processing, and Police Clearance Certificates (PCC).",
        "description_tamil": "புதிய இந்திய பாஸ்போர்ட் விண்ணப்பம், புதுப்பித்தல், தட்கல் விரைவு சேவை மற்றும் போலீஸ் சான்றொப்பம் (PCC).",
        "eligibility": [
            "Indian citizens by birth, descent, registration, or naturalization."
        ],
        "required_documents": [
            "Proof of Date of Birth: Birth certificate, School leaving certificate, Aadhaar.",
            "Proof of Present Address: Aadhaar, Water/Electricity bill, Bank passbook.",
            "Non-ECR (Emigration Check Not Required) Proof: 10th standard educational certificate or higher degree."
        ],
        "step_by_step_process": [
            "Register on the official Passport Seva portal (passportindia.gov.in) or mPassport Seva App.",
            "Fill Application Form for Fresh / Reissue and submit details.",
            "Book an appointment slot at the nearest Passport Seva Kendra (PSK) or Post Office PSK (POPSK).",
            "Make payment online to confirm the appointment slot.",
            "Visit PSK with original documents for biometric capture and photograph.",
            "Police verification is carried out at applicant's current residence.",
            "Passport dispatched via India Post Speed Post with SMS tracking."
        ],
        "relevant_authority": "Consular, Passport & Visa Division, Ministry of External Affairs (MEA)",
        "official_portal_name": "Passport Seva Kendra Portal",
        "official_url_demo": "https://www.passportindia.gov.in",
        "processing_time": "Standard: 15–30 days; Tatkaal: 1–3 business days.",
        "fee_structure": "Standard 36-page booklet (10 yrs): Rs 1,500; Tatkaal: Additional Rs 2,000."
    },
    {
        "id": "voter-services",
        "title": "Voter Registration & Services (VHA)",
        "title_tamil": "வாக்காளர் அடையாள அட்டை சேவைகள்",
        "category": "Electoral & Democratic Rights",
        "icon": "Vote",
        "description": "Enrollment of new voters (Form 6), corrections in electoral roll (Form 8), shifting of constituency, and downloading digital e-EPIC card.",
        "description_tamil": "புதிய வாக்காளர் பதிவு (படிவம் 6), பெயர் திருத்தம் மற்றும் தொகுதி மாற்றம் (படிவம் 8), டிஜிட்டல் e-EPIC பதிவிறக்கம்.",
        "eligibility": [
            "Indian citizen aged 18 years or above on qualifying dates (Jan 1, Apr 1, Jul 1, Oct 1).",
            "Resident of the designated polling constituency."
        ],
        "required_documents": [
            "Passport-size photograph.",
            "Proof of Age: Birth certificate, Aadhaar, PAN card, Driving Licence, Class 10 mark sheet.",
            "Proof of Ordinary Residence: Electricity bill, Water bill, Aadhaar, Ration card."
        ],
        "step_by_step_process": [
            "Visit the Election Commission portal (voters.eci.gov.in) or Voter Helpline Mobile App.",
            "Select Form 6 for New Voter Registration.",
            "Upload photograph, age proof, and address proof documents.",
            "Submit application and receive an acknowledgement Reference ID.",
            "Booth Level Officer (BLO) performs field verification at your doorstep.",
            "Upon approval by Electoral Registration Officer (ERO), EPIC card is printed and delivered by Speed Post."
        ],
        "relevant_authority": "Election Commission of India (ECI) & State Chief Electoral Officers",
        "official_portal_name": "ECI Voters Service Portal",
        "official_url_demo": "https://voters.eci.gov.in",
        "processing_time": "15 to 30 days depending on electoral revision cycles.",
        "fee_structure": "Completely free of cost for all Indian citizens."
    },
    {
        "id": "driving-licence-services",
        "title": "Driving Licence & Parivahan",
        "title_tamil": "ஓட்டுநர் உரிமம் மற்றும் பரிவஹன்",
        "category": "Transport & Mobility",
        "icon": "Car",
        "description": "Learner's Licence (LLR) online exam from home, Permanent Driving Licence slot booking, vehicle registration, and renewal.",
        "description_tamil": "வீட்டிலிருந்தே பழகுநர் உரிமம் (LLR) ஆன்லைன் தேர்வு, நிரந்தர ஓட்டுநர் உரிமம் முன்பதிவு மற்றும் புதுப்பித்தல்.",
        "eligibility": [
            "Age 16+ for gearless 2-wheelers up to 50cc; Age 18+ for light motor vehicles (cars/motorcycles); Age 20+ for transport vehicles."
        ],
        "required_documents": [
            "Age Proof: Birth certificate, SSLC marksheet, Aadhaar.",
            "Address Proof: Aadhaar card, Passport, Voter ID, Electricity bill.",
            "Medical Certificate (Form 1A for applicants over 40 years or commercial licences)."
        ],
        "step_by_step_process": [
            "Visit Parivahan Sarathi portal (sarathi.parivahan.gov.in) and choose your State.",
            "Apply for Learner's Licence (LLR) using Aadhaar authentication (no RTO visit needed in most states).",
            "Take the online road safety video tutorial and traffic rules multiple-choice quiz.",
            "Download instant Learner's Licence upon passing quiz.",
            "After 30 days (valid for 6 months), book driving test appointment for Permanent Driving Licence.",
            "Attend vehicle driving test at designated RTO track; Smart card dispatched upon passing."
        ],
        "relevant_authority": "Ministry of Road Transport and Highways (MoRTH) & State Transport Departments",
        "official_portal_name": "Parivahan Sarathi Portal",
        "official_url_demo": "https://sarathi.parivahan.gov.in",
        "processing_time": "LLR: Same day online; Driving Licence: 7 to 15 days post driving test.",
        "fee_structure": "LLR approx Rs 150 to Rs 200; Driving test & Smart card licence approx Rs 700 to Rs 1,000."
    },
    {
        "id": "certificates-edistrict",
        "title": "Government Certificates (e-District)",
        "title_tamil": "அரசு சான்றிதழ்கள் (வருமானம், சாதி, இருப்பிடம்)",
        "category": "Civic & Revenue Services",
        "icon": "Award",
        "description": "Issuance of digitally signed Income, Community/Caste, Nativity/Residence, First Graduate, and Legal Heir certificates via State e-Sevai / e-District portals.",
        "description_tamil": "வருமானச் சான்றிதழ், சாதிச் சான்றிதழ், இருப்பிடச் சான்று, முதல் பட்டதாரி மற்றும் வாரிசு சான்றிதழ்கள்.",
        "eligibility": [
            "Permanent residents and domicile holders of the respective state / union territory."
        ],
        "required_documents": [
            "Aadhaar card of applicant and head of family.",
            "Ration card / Smart Family card.",
            "Salary slip / IT Return / Self-declaration for Income Certificate.",
            "Parent's or sibling's Community Certificate for Caste Certificate.",
            "Death Certificate for Legal Heir certificate."
        ],
        "step_by_step_process": [
            "Login to State e-District / e-Sevai citizen portal or visit nearest Common Service Centre (CSC).",
            "Choose desired certificate (Income, Community, Nativity, Legal Heir, etc.).",
            "Upload scanned documents and make nominal fee payment (approx Rs 60).",
            "Application routed digitally to Village Administrative Officer (VAO) -> Revenue Inspector (RI) -> Tahsildar.",
            "Download QR-code verified digitally signed certificate from portal."
        ],
        "relevant_authority": "Revenue and Disaster Management Department of State Governments",
        "official_portal_name": "State e-District / e-Sevai Portals (e.g. tnesevai.tn.gov.in)",
        "official_url_demo": "https://edistrict.gov.in",
        "processing_time": "7 to 15 business days depending on service level agreement (Citizen Charter).",
        "fee_structure": "Government portal fee Rs 50 to Rs 60."
    },
    {
        "id": "cpgrams-grievance",
        "title": "Public Grievance Redressal (CPGRAMS)",
        "title_tamil": "பொதுக் குறைகள் தீர்க்கும் மையம் (CPGRAMS)",
        "category": "Grievance & Accountability",
        "icon": "MessageSquareWarning",
        "description": "Centralized 24x7 online platform to lodge grievances against any Central/State Ministry, Department, Bank, Railway, or Public Sector Undertaking.",
        "description_tamil": "மத்திய, மாநில அரசு துறைகள், வங்கிகள் மற்றும் ரயில்வே மீதான குறைகளை ஆன்லைனில் தீர்க்கும் முறைமை.",
        "eligibility": [
            "Any citizen of India facing unresolved administrative grievances with public authorities."
        ],
        "required_documents": [
            "Grievance petition text detailing issue, previous complaint reference numbers, and department involved.",
            "Scanned PDF copies of past correspondence or unanswered petitions (Max 4MB)."
        ],
        "step_by_step_process": [
            "Register on pgportal.gov.in with name and mobile number.",
            "Click 'Lodge Public Grievance' and select the concerned Ministry/Department.",
            "Write the complaint clearly with chronological timeline.",
            "Upload supporting PDFs and submit to generate a unique Registration Number.",
            "Department is mandated to resolve within 30 days.",
            "If dissatisfied with resolution, file an Appeal within 30 days before Appellate Authority."
        ],
        "relevant_authority": "Department of Administrative Reforms and Public Grievances (DARPG)",
        "official_portal_name": "CPGRAMS Portal",
        "official_url_demo": "https://pgportal.gov.in",
        "processing_time": "Mandated resolution timeframe within 30 calendar days.",
        "fee_structure": "Completely free service."
    },
    {
        "id": "rti-online-service",
        "title": "RTI Online Filing",
        "title_tamil": "ஆன்லைன் தகவல் அறியும் உரிமை (RTI Online)",
        "category": "Transparency & Governance",
        "icon": "FileCheck",
        "description": "Filing Right to Information applications and First Appeals online for all Central Ministries, Departments, and Public Authorities.",
        "description_tamil": "மத்திய அரசு அலுவலகங்களிடம் ஆன்லைன் மூலம் தகவல் கோரும் விண்ணப்பம் மற்றும் முதல் மேல்முறையீடு.",
        "eligibility": [
            "Every citizen of India."
        ],
        "required_documents": [
            "Concise list of specific queries/documents requested (under 3000 characters).",
            "BPL Card / Certificate for fee exemption (if claiming exemption)."
        ],
        "step_by_step_process": [
            "Visit rtionline.gov.in and click 'Submit Request'.",
            "Read guidelines and accept declarations.",
            "Select the Ministry/Department/Apex body from the dropdown.",
            "Type your questions seeking certified records, orders, or copies of files.",
            "Pay statutory fee of Rs 10 via UPI, Netbanking, or Debit card (exempt for BPL).",
            "Download unique Registration Number and track 30-day response progress."
        ],
        "relevant_authority": "Department of Personnel & Training (DoPT), Government of India",
        "official_portal_name": "RTI Online Portal",
        "official_url_demo": "https://rtionline.gov.in",
        "processing_time": "30 days statutory deadline (48 hours if life and liberty is involved).",
        "fee_structure": "Statutory application fee: Rs 10 (Free for BPL category)."
    }
]

def get_all_services():
    return GOVERNMENT_SERVICES

def get_service_by_id(srv_id: str):
    for srv in GOVERNMENT_SERVICES:
        if srv["id"] == srv_id:
            return srv
    return None
