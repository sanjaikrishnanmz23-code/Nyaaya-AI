"""
Guided Problem Resolution Workflows ("What Should I Do?")
Step-by-step action guides for acute citizen issues with progressive timelines.
"""

PROBLEM_ACTION_GUIDES = [
    {
        "id": "salary-not-paid",
        "title": "Salary Not Paid / Withheld",
        "title_tamil": "சம்பளம் கொடுக்கப்படவில்லை / நிறுத்தி வைக்கப்பட்டுள்ளது",
        "icon": "WalletCards",
        "urgency_level": "High",
        "helpline": "1800-425-3711",
        "helpline_name": "Labour Grievance Cell",
        "summary": "Step-by-step roadmap when an employer withholds wages, delays payment beyond statutory limits, or refuses full and final settlement.",
        "summary_tamil": "முதலாளி சம்பளம் தர மறுத்தால் அல்லது காலதாமதம் செய்தால் சட்டப்படி என்ன செய்ய வேண்டும் என்பதற்கான வழிகாட்டி.",
        "timeline_steps": [
            {
                "stage": "Step 1: Immediate",
                "stage_tamil": "படி 1: உடனடி நடவடிக்கை",
                "title": "Document & Check Contract",
                "title_tamil": "ஆவணங்களை சேகரித்து ஒப்பந்தத்தை சரிபார்க்கவும்",
                "desc": "Download all past payslips, attendance records, Form 26AS/PF deposits, offer letter, and employment contract. Note exact dues.",
                "desc_tamil": "முந்தைய சம்பள சீட்டுகள், வருகை பதிவேடு, பிஎஃப் விவரங்கள் மற்றும் பணி ஒப்பந்த நகல்களை பதிவிறக்கம் செய்து பாதுகாக்கவும்."
            },
            {
                "stage": "Step 2: Formal Notice",
                "stage_tamil": "படி 2: எழுத்துப்பூர்வ அறிவிப்பு",
                "title": "Send Written Demand Email",
                "title_tamil": "அதிகாரப்பூர்வ கோரிக்கை மின்னஞ்சல் அனுப்பவும்",
                "desc": "Send a professional email to HR and Finance specifying overdue amount, statutory deadline (Section 5, Payment of Wages Act), giving 7–10 days.",
                "desc_tamil": "ஊதிய பட்டுவாடா சட்டத்தை குறிப்பிட்டு, 7 முதல் 10 நாட்களுக்குள் நிலுவை தொகையை விடுவிக்குமாறு நிறுவனத்திற்கு மின்னஞ்சல் அனுப்பவும்."
            },
            {
                "stage": "Step 3: Portal Complaint",
                "stage_tamil": "படி 3: அரசு போர்ட்டலில் புகார்",
                "title": "File on Samadhan Portal",
                "title_tamil": "தொழிலாளர் சமாதான் போர்ட்டலில் பதிவு செய்யவும்",
                "desc": "Submit an online industrial dispute/claim petition on the Ministry of Labour Samadhan portal (samadhan.labour.gov.in).",
                "desc_tamil": "மத்திய தொழிலாளர் அமைச்சகத்தின் சமாதான் இணையதளத்தில் நிறுவனத்தின் மீது முறைப்படி புகார் பதிவு செய்யவும்."
            },
            {
                "stage": "Step 4: Legal Claim",
                "stage_tamil": "படி 4: சட்ட நடவடிக்கை",
                "title": "Labour Commissioner Petition",
                "title_tamil": "தொழிலாளர் ஆணையரிடம் வழக்கு தாக்கல்",
                "desc": "File an application under Section 15 of Payment of Wages Act or Section 33C(2) of Industrial Disputes Act before the jurisdictional Labour Commissioner.",
                "desc_tamil": "வட்டார தொழிலாளர் ஆணையர் முன்னிலையில் இழப்பீட்டுடன் கூடிய சம்பள மீட்பு மனு தாக்கல் செய்யவும்."
            }
        ],
        "do_this_first": [
            "Download all company email communications, chat records, and task completion proofs to a personal drive before systems access is revoked.",
            "Obtain your latest bank account statement showing the zero credit for the missing pay cycle.",
            "Verify whether Provident Fund (PF) and ESI deductions were actually credited to your EPFO passbook."
        ],
        "do_next": [
            "Send a polite but firm written communication to the HR Head and Managing Director outlining unpaid dues.",
            "Give a clear timeline of 7 to 15 calendar days for credit transfer.",
            "State clearly that continued non-payment will compel you to seek statutory intervention under the Payment of Wages Act."
        ],
        "then_step": [
            "If no response or unsatisfactory reply, file an online grievance on the Ministry of Labour Samadhan Portal (samadhan.labour.gov.in).",
            "Serve a formal Legal Notice through a practicing advocate or legal aid counsel.",
            "File a complaint with the Labour Enforcement Officer (LEO) of your district."
        ],
        "follow_up": [
            "Attend the conciliation meeting summoned by the Labour Officer.",
            "If conciliation fails, request a Failure of Conciliation (FOC) report to approach the Labour Court for recovery certificate.",
            "Under Section 15(3) of Payment of Wages Act, you may claim compensation up to 10 times the withheld amount."
        ],
        "documents_checklist": [
            "Offer Letter & Appointment Order",
            "Latest 3 to 6 months Payslips",
            "Bank Statement reflecting non-credit",
            "Attendance / Timesheet logs",
            "Copy of resignation or termination letter (if applicable)",
            "EPFO UAN Statement"
        ]
    },
    {
        "id": "online-fraud",
        "title": "Online Fraud & Financial Scam",
        "title_tamil": "ஆன்லைன் மோசடி மற்றும் வங்கி நிதி இழப்பு",
        "icon": "ShieldAlert",
        "urgency_level": "Critical",
        "helpline": "1930",
        "helpline_name": "National Cyber Crime Helpline (24x7)",
        "summary": "Urgent emergency action plan for unauthorized UPI debits, credit card frauds, phishing, and fake investment traps.",
        "summary_tamil": "UPI மோசடி, கார்டு தகவல் திருட்டு அல்லது போலி முதலீட்டு மோசடிகளில் பணம் இழந்தால் முதல் 2 மணி நேரத்தில் எடுக்க வேண்டிய நடவடிக்கைகள்.",
        "timeline_steps": [
            {
                "stage": "First 15 Minutes",
                "stage_tamil": "முதல் 15 நிமிடங்கள்",
                "title": "Freeze & Call 1930",
                "title_tamil": "வங்கி கணக்கை முடக்கி 1930-ஐ அழைக்கவும்",
                "desc": "Call 1930 immediately to trigger the National Cyber Financial Management (CFCFRMS) system to freeze beneficiary accounts.",
                "desc_tamil": "உடனடியாக 1930 எண்ணை அழைத்து பரிவர்த்தனை விவரங்களை கூறி எதிர்தரப்பு வங்கி கணக்கை முடக்கச் சொல்லவும்."
            },
            {
                "stage": "Within 1 Hour",
                "stage_tamil": "1 மணி நேரத்திற்குள்",
                "title": "Block Banking Credentials",
                "title_tamil": "வங்கி அட்டை/UPI-ஐ பிளாக் செய்யவும்",
                "desc": "Block UPI ID, debit/credit cards, and netbanking access through your mobile banking application or phone banking.",
                "desc_tamil": "வங்கி செயலி அல்லது வாடிக்கையாளர் சேவை மூலம் உங்கள் கார்டுகள் மற்றும் நெட் பேங்கிங்கை பிளாக் செய்யவும்."
            },
            {
                "stage": "Within 24 Hours",
                "stage_tamil": "24 மணி நேரத்திற்குள்",
                "title": "Lodge Cybercrime Portal Complaint",
                "title_tamil": "சைபர் போர்ட்டலில் அதிகாரப்பூர்வ புகார்",
                "desc": "Register detailed formal complaint on cybercrime.gov.in uploading transaction UTR receipts and screenshots.",
                "desc_tamil": "cybercrime.gov.in இணையத்தில் UTR எண்கள் மற்றும் ஆதாரங்களுடன் விரிவான புகார் பதிவு செய்யவும்."
            },
            {
                "stage": "Follow-Up: 3 Days",
                "stage_tamil": "3 நாட்களுக்குள்",
                "title": "Bank Zero Liability Claim",
                "title_tamil": "வங்கியிடம் இழப்பீடு கோரிக்கை",
                "desc": "Submit written notice with FIR copy to bank under RBI Circular on Limited Liability of Customers in Unauthorized Electronic Banking.",
                "desc_tamil": "RBI-யின் வாடிக்கையாளர் பொறுப்பு பாதுகாப்பு விதிகளின்படி வங்கியிடம் எழுத்துப்பூர்வ நிவாரண மனு தாக்கல் செய்யவும்."
            }
        ],
        "do_this_first": [
            "Dial 1930 without a single minute of delay. The first 2 hours are the 'Golden Period' when money can be frozen before withdrawal at ATMs.",
            "Provide the operator: Your Bank Name, Account Number, Debited Amount, Transaction Date & Time, and UTR/Reference ID from the debit SMS.",
            "Lock your Aadhaar biometrics instantly on the mAadhaar app if AePS (fingerprint debit) was used."
        ],
        "do_next": [
            "Open your mobile banking app and freeze all cards, disable international transactions, and change Netbanking/UPI MPINs.",
            "Take crisp screenshots of fraudulent payment requests, WhatsApp chats, fake app icons, phishing SMS, and caller numbers.",
            "Never delete SMS threads or WhatsApp conversations with scammers as they are vital primary forensic evidence."
        ],
        "then_step": [
            "File an e-complaint on the national portal (cybercrime.gov.in) under 'Report Cyber Financial Fraud'.",
            "Keep the generated acknowledgement PDF safe.",
            "Submit a formal written dispute (Chargeback form) at your bank branch within 3 days to invoke RBI Zero-Liability protection."
        ],
        "follow_up": [
            "Track the status of the frozen money through the investigating officer of your local Cyber Crime Police Station.",
            "File an application under Section 457 CrPC / BNSS before the Magistrate Court to obtain a release order for the frozen amount.",
            "If your bank failed in safety compliance, escalate to the RBI Banking Ombudsman (cms.rbi.org.in)."
        ],
        "documents_checklist": [
            "Bank account statement highlighting unauthorized debits",
            "Transaction IDs / UTR / Reference numbers",
            "SMS alerts received from the bank",
            "Cybercrime.gov.in acknowledgement slip",
            "Identity Proof (Aadhaar / Voter ID)"
        ]
    },
    {
        "id": "consumer-complaint",
        "title": "Consumer Dispute & Defective Product",
        "title_tamil": "நுகர்வோர் குறைபாடு மற்றும் ஏமாற்று வர்த்தகம்",
        "icon": "ShoppingCart",
        "urgency_level": "Standard",
        "helpline": "1915",
        "helpline_name": "National Consumer Helpline (NCH)",
        "summary": "Systematic redressal process for defective electronics, rejected warranty claims, e-commerce delivery frauds, and overcharging.",
        "summary_tamil": "வாங்கிய பொருளில் குறைபாடு அல்லது உத்தரவாதத்தை (Warranty) நிறுவனம் மறுத்தால் பணத்தை திரும்பப் பெறும் வழிமுறை.",
        "timeline_steps": [
            {
                "stage": "Day 1–3",
                "stage_tamil": "நாள் 1–3",
                "title": "Evidence & Grievance Officer",
                "title_tamil": "ஆதாரங்களை சேகரித்து நிறுவனத்திற்கு தகவல்",
                "desc": "Collect bill, warranty card, unboxing video. Email the manufacturer/seller Grievance Officer with 7-day refund notice.",
                "desc_tamil": "பில், வாரண்டி அட்டை மற்றும் குறைபாட்டின் வீடியோவை நிறுவனத்தின் குறைதீர்க்கும் அதிகாரிக்கு அனுப்பி தீர்வு கேட்கவும்."
            },
            {
                "stage": "Day 4–7",
                "stage_tamil": "நாள் 4–7",
                "title": "Call 1915 NCH Helpline",
                "title_tamil": "1915 நுகர்வோர் உதவி மையத்தை அழைக்கவும்",
                "desc": "Register a docket number with National Consumer Helpline via phone (1915), WhatsApp (8800001915), or INGRAM portal.",
                "desc_tamil": "தேசிய நுகர்வோர் உதவி எண் 1915 அல்லது வாட்ஸ்அப் (8800001915) மூலம் அதிகாரப்பூர்வ புகார் பதிவு செய்யவும்."
            },
            {
                "stage": "Day 15–30",
                "stage_tamil": "நாள் 15–30",
                "title": "Legal Notice",
                "title_tamil": "சட்டப்பூர்வ நோட்டீஸ்",
                "desc": "Issue a legal notice citing Consumer Protection Act 2019 claiming replacement, full refund, and compensation for mental agony.",
                "desc_tamil": "நுகர்வோர் பாதுகாப்பு சட்டத்தின்படி இழப்பீடு மற்றும் பணத்தைத் திருப்பித் தரக் கோரி நோட்டீஸ் அனுப்பவும்."
            },
            {
                "stage": "Day 30+",
                "stage_tamil": "நாள் 30க்கு மேல்",
                "title": "File on e-Daakhil",
                "title_tamil": "e-Daakhil மூலம் வழக்கு தொடரவும்",
                "desc": "File an online case directly before the District Consumer Commission via edaakhil.nic.in without paying heavy advocate fees.",
                "desc_tamil": "edaakhil.nic.in இணையம் மூலம் உங்கள் மாவட்ட நுகர்வோர் நீதிமன்றத்தில் எளிய கட்டணத்தில் நேரடியாக வழக்கு தொடரலாம்."
            }
        ],
        "do_this_first": [
            "Locate and scan the original tax invoice, delivery packing slip, serial number, and payment confirmation receipt.",
            "Record clear photographs or videos illustrating the malfunction, defect, or deviation from advertised specifications.",
            "Stop using the defective product to avoid allegations of user-inflicted physical damage."
        ],
        "do_next": [
            "Write an email to the customer support desk with CC to the statutory Grievance Officer (mandatory on all Indian e-commerce portals).",
            "State clearly: Defect description, attempts made to resolve, and request for full refund or replacement within 7 working days.",
            "Save all automated ticket numbers and email exchanges."
        ],
        "then_step": [
            "Call the National Consumer Helpline at 1915 (9:30 AM to 5:30 PM, all days except national holidays) or register on consumerhelpline.gov.in.",
            "NCH mediates between the consumer and registered corporate brands with high pre-litigation resolution rates."
        ],
        "follow_up": [
            "If the seller or manufacturer refuses to resolve, file an e-complaint on the government e-Daakhil portal (edaakhil.nic.in).",
            "You can represent yourself without hiring an advocate. The District Commission can order refund, replacement, punitive damages, and litigation costs."
        ],
        "documents_checklist": [
            "Tax Invoice / Retail Bill",
            "Warranty Card / Service Job Card",
            "Photographs & Video proof of defect",
            "Email correspondence with seller/manufacturer",
            "NCH Complaint Docket Number"
        ]
    },
    {
        "id": "police-encounter",
        "title": "Police Questioning, Stop or Detention",
        "title_tamil": "காவல்துறை விசாரணை, தடுத்து நிறுத்துதல் அல்லது கைது",
        "icon": "ShieldAlert",
        "urgency_level": "Critical",
        "helpline": "15100",
        "helpline_name": "NALSA Free Legal Aid Helpline",
        "summary": "Clear, lawful rights and actions when stopped on the road, summoned for questioning, or subjected to arbitrary police detention.",
        "summary_tamil": "காவல்துறையினர் வாகன சோதனையின் போதோ அல்லது காவல் நிலையத்திற்கு அழைக்கும் போதோ உங்கள் சட்டப்பூர்வ உரிமைகள்.",
        "timeline_steps": [
            {
                "stage": "On the Spot",
                "stage_tamil": "சம்பவ இடத்தில்",
                "title": "Remain Calm & Ask Identity",
                "title_tamil": "அமைதி காத்து அடையாளத்தை கேட்கவும்",
                "desc": "Politely ask for the officer's name, designation, and reason for stop. Do not resist physically or argue aggressively.",
                "desc_tamil": "காவலரின் பெயர், பதவி மற்றும் நிறுத்தியதற்கான காரணத்தை கண்ணியமாக கேட்கவும். வாக்குவாதத்தில் ஈடுபட வேண்டாம்."
            },
            {
                "stage": "If Detained",
                "stage_tamil": "காவல் வைக்கப்பட்டால்",
                "title": "Demand Arrest Memo",
                "title_tamil": "கைது ஆவணம் (Arrest Memo) கேட்கவும்",
                "desc": "Under D.K. Basu guidelines, police MUST prepare an Arrest Memo indicating date, time, and location, counter-signed by a respectable witness.",
                "desc_tamil": "டி.கே. பாசு வழிகாட்டுதலின்படி நேரம் மற்றும் காரணத்துடன் கூடிய Arrest Memo தயாரித்து சாட்சி கையெழுத்து இட வேண்டும்."
            },
            {
                "stage": "Immediate Right",
                "stage_tamil": "உடனடி உரிமை",
                "title": "Inform Family & Advocate",
                "title_tamil": "குடும்பத்தினருக்கும் வழக்கறிஞருக்கும் தகவல்",
                "desc": "Section 50A CrPC/BNSS gives you the absolute right to have one family member or friend informed of your location and custody status.",
                "desc_tamil": "பிரிவு 50A-ன் கீழ் நீங்கள் இருக்கும் இடம் மற்றும் காவல் விவரங்களை குடும்பத்தினர் ஒருவருக்கு தெரிவிக்க முழு உரிமை உண்டு."
            },
            {
                "stage": "Within 24 Hours",
                "stage_tamil": "24 மணி நேரத்திற்குள்",
                "title": "Magistrate Production",
                "title_tamil": "மாஜிஸ்திரேட் முன் ஆஜர்படுத்துதல்",
                "desc": "Article 22(2) Constitution mandates production before nearest Judicial Magistrate within 24 hours (excluding travel time).",
                "desc_tamil": "அரசியலமைப்பு பிரிவு 22(2) இன் படி 24 மணி நேரத்திற்குள் நீதிமன்ற நீதிபதி (மாஜிஸ்திரேட்) முன் ஆஜர்படுத்தப்பட வேண்டும்."
            }
        ],
        "do_this_first": [
            "Stay composed and polite. Never use physical force, flee, or escalate confrontation.",
            "Memorize or note down the officer's uniform name-plate, batch number, and vehicle registration number.",
            "Ask politely: 'Officer, am I free to go, or am I being detained or arrested?'"
        ],
        "do_next": [
            "If arrested, demand the preparation of an Arrest Memo with the exact time and location.",
            "Refuse to sign blank papers or pre-typed self-incriminating confessions (confessions made to police are inadmissible in court under Indian Evidence Act).",
            "Exercise your right to have a relative or friend notified immediately by the police station duty officer."
        ],
        "then_step": [
            "Request a medical examination by a government medical officer at the time of arrest and before production to document lack of injuries.",
            "If you cannot afford a private lawyer, state before the Magistrate: 'I request free legal aid counsel from DLSA (District Legal Services Authority)'.",
            "Female citizens: No woman can be arrested between sunset and sunrise without special magistrate permission and presence of a woman police officer."
        ],
        "follow_up": [
            "Report custodial harassment, extortion, or brutality to the Police Complaints Authority (PCA) or State Human Rights Commission.",
            "Obtain a certified copy of the FIR and Remand Application from the Magistrate Court."
        ],
        "documents_checklist": [
            "Aadhaar / Voter ID (Identity Proof)",
            "Copy of Arrest Memo (mandatory copy to arrestee)",
            "Free copy of FIR (mandatory under Section 154 CrPC)",
            "Medical Inspection Report"
        ]
    },
    {
        "id": "government-delay-bribe",
        "title": "Government Delay, Inaction or Bribe Demand",
        "title_tamil": "அரசு அலுவலக காலதாமதம் அல்லது லஞ்சக் கோரிக்கை",
        "icon": "Building2",
        "urgency_level": "High",
        "helpline": "1064",
        "helpline_name": "Anti-Corruption Bureau (ACB / DVAC)",
        "summary": "Remedies when government officials refuse to process certificates, delay lawful files indefinitely, or demand corrupt speed money.",
        "summary_tamil": "அரசு அலுவலகத்தில் சான்றிதழ் வழங்க தாமதம் செய்தாலோ அல்லது லஞ்சம் கேட்டாலோ புகார் செய்யும் முறை.",
        "timeline_steps": [
            {
                "stage": "Step 1",
                "stage_tamil": "படி 1",
                "title": "Check Citizen's Charter",
                "title_tamil": "குடிமக்கள் சாசன காலக்கெடுவை சரிபார்க்கவும்",
                "desc": "Check the statutory time limit (Citizen's Charter) for the service. Note your Application ID and submission date.",
                "desc_tamil": "அந்த சான்றிதழுக்கான அரசு காலக்கெடுவை (Citizen's Charter) சரிபார்த்து விண்ணப்ப எண்ணை குறித்துக் கொள்ளவும்."
            },
            {
                "stage": "Step 2",
                "stage_tamil": "படி 2",
                "title": "File RTI on File Status",
                "title_tamil": "RTI மூலம் கோப்பு நிலையை கேட்கவும்",
                "desc": "File an RTI application asking: 'Provide daily progress report and names of officials with whom my file remained pending.'",
                "desc_tamil": "RTI மூலம் 'எனது மனு எந்தெந்த அதிகாரிகள் மேசையில் எத்தனை நாட்கள் நிலுவையில் இருந்தது?' என்று கேள்வி கேட்கவும்."
            },
            {
                "stage": "Step 3",
                "stage_tamil": "படி 3",
                "title": "CPGRAMS / CM Cell",
                "title_tamil": "முதல்வர் தனிப்பிரிவு / CPGRAMS-ல் புகார்",
                "desc": "Lodge an online grievance on the State CM Cell / e-Parihar portal or Central CPGRAMS (pgportal.gov.in).",
                "desc_tamil": "மாநில முதல்வர் தனிப்பிரிவு (CM Cell) அல்லது CPGRAMS போர்ட்டலில் அதிகாரி மீது புகார் பதிவு செய்யவும்."
            },
            {
                "stage": "Step 4",
                "stage_tamil": "படி 4",
                "title": "Alert Anti-Corruption",
                "title_tamil": "லஞ்ச ஒழிப்புத் துறையை அணுகவும்",
                "desc": "If bribe is demanded, contact Anti-Corruption Bureau (ACB) / Directorate of Vigilance and Anti-Corruption (DVAC) at 1064 for trap operations.",
                "desc_tamil": "லஞ்சம் கேட்கப்பட்டால் 1064 என்ற எண்ணில் லஞ்ச ஒழிப்புத் துறையை (DVAC/ACB) தொடர்பு கொண்டு புகார் அளிக்கலாம்."
            }
        ],
        "do_this_first": [
            "Never pay a bribe. Paying a bribe is also punishable under the Prevention of Corruption Act.",
            "Record date, time, and application reference number of your original submission.",
            "Check the state Right to Public Services Act (RTS Act) or Citizen's Charter for statutory delivery timeline."
        ],
        "do_next": [
            "Meet the higher supervisory officer (Tahsildar, Revenue Divisional Officer, District Collector, or Department Head) on public grievance days (usually Mondays).",
            "File an RTI application asking: 'State the day-to-day progress of application ID XXXX, name and designation of officers who handled the file, and reasons for delay beyond Citizen Charter timeline'."
        ],
        "then_step": [
            "Lodge a petition on the State Chief Minister's Grievance Cell (e.g. CM Special Cell / Mudhalvar Mugavari in TN, Jan Samwad, etc.) and pgportal.gov.in.",
            "If an official demands illegal gratification, immediately contact the State Vigilance and Anti-Corruption Directorate (DVAC / ACB helpline 1064). Trap operations are conducted free of cost."
        ],
        "follow_up": [
            "The Prevention of Corruption Act protects citizens who report extortionary bribe demands within 7 days.",
            "Track your CPGRAMS grievance until final disposal; escalate to the Appellate Authority if closed prematurely."
        ],
        "documents_checklist": [
            "Application submission acknowledgement slip",
            "Payment receipt for government fees",
            "Copy of previous petitions submitted",
            "Citizen Charter printout showing maximum processing days"
        ]
    }
]

def get_all_action_guides():
    return PROBLEM_ACTION_GUIDES

def get_action_guide_by_id(guide_id: str):
    for guide in PROBLEM_ACTION_GUIDES:
        if guide["id"] == guide_id:
            return guide
    return None
