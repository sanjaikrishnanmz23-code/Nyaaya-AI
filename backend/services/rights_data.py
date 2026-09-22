"""
Comprehensive Indian Citizen Rights Database
Structured across 10 official categories with bilingual details (English & Tamil).
"""

RIGHTS_CATEGORIES = [
    {
        "id": "fundamental-rights",
        "title": "Fundamental Rights",
        "title_tamil": "அடிப்படை உரிமைகள்",
        "icon": "Scale",
        "badge": "Articles 14–32",
        "short_desc": "Constitutional guarantees of equality, freedom of speech, personal liberty, and protection against discrimination.",
        "short_desc_tamil": "சமத்துவம், பேச்சுரிமை, தனிமனித சுதந்திரம் மற்றும் பாகுபாட்டிற்கு எதிரான அரசியலமைப்பு உத்தரவாதங்கள்.",
        "overview": "Part III of the Constitution of India guarantees six fundamental rights to every citizen. These rights are legally enforceable directly through the High Courts (Article 226) and Supreme Court (Article 32) under constitutional writ jurisdiction.",
        "overview_tamil": "இந்திய அரசியலமைப்பின் பகுதி III ஒவ்வொரு குடிமகனுக்கும் ஆறு அடிப்படை உரிமைகளை உத்தரவாதம் செய்கிறது. இந்த உரிமைகள் மீறப்பட்டால் உயர் நீதிமன்றம் (பிரிவு 226) மற்றும் உச்ச நீதிமன்றத்தை (பிரிவு 32) நேரடியாக அணுகி நீதி பெறலாம்.",
        "common_questions": [
            {
                "q": "What are my basic fundamental rights?",
                "q_ta": "எனது அடிப்படை உரிமைகள் என்னென்ன?",
                "a": "Right to Equality (Art 14-18), Right to Freedom (Art 19-22), Right against Exploitation (Art 23-24), Right to Freedom of Religion (Art 25-28), Cultural and Educational Rights (Art 29-30), and Right to Constitutional Remedies (Art 32).",
                "a_ta": "சமத்துவ உரிமை (பிரிவுகள் 14-18), சுதந்திர உரிமை (பிரிவுகள் 19-22), சுரண்டலுக்கு எதிரான உரிமை (பிரிவுகள் 23-24), மத சுதந்திர உரிமை (பிரிவுகள் 25-28), கலாச்சார மற்றும் கல்வி உரிமைகள் (பிரிவுகள் 29-30), அரசியலமைப்பு தீர்வு உரிமை (பிரிவு 32)."
            },
            {
                "q": "What can I do if any fundamental right is violated?",
                "q_ta": "அடிப்படை உரிமை மீறப்பட்டால் நான் என்ன செய்ய வேண்டும்?",
                "a": "You can file a Writ Petition (Habeas Corpus, Mandamus, Prohibition, Quo Warranto, Certiorari) directly before the High Court under Article 226 or Supreme Court under Article 32.",
                "a_ta": "உயர் நீதிமன்றத்தில் பிரிவு 226 அல்லது உச்ச நீதிமன்றத்தில் பிரிவு 32 இன் கீழ் ஆட்கொணர்வு, கட்டளை அல்லது தடையுறுத்து போன்ற நீதிப்பேராணை (Writ Petition) மனு தாக்கல் செய்யலாம்."
            }
        ],
        "citizen_actions": [
            "Document any arbitrary action, discrimination, or violation by a public authority.",
            "Send a legal notice through an advocate or legal aid counsel.",
            "File a Public Interest Litigation (PIL) if a large section of citizens is affected.",
            "Approach the State Human Rights Commission (SHRC) or National Human Rights Commission (NHRC)."
        ],
        "citizen_actions_tamil": [
            "அரசு அதிகாரியின் தன்னிச்சையான அல்லது பாகுபாடான நடவடிக்கையை ஆவணப்படுத்தவும்.",
            "வழக்கறிஞர் அல்லது இலவச சட்ட உதவி மையம் மூலம் சட்டப்பூர்வ நோட்டீஸ் அனுப்பவும்.",
            "பொதுமக்கள் பெருமளவில் பாதிக்கப்பட்டால் பொதுநல வழக்கு (PIL) தொடரலாம்.",
            "மாநில அல்லது தேசிய மனித உரிமைகள் ஆணையத்தில் புகார் அளிக்கலாம்."
        ],
        "relevant_authorities": [
            "Supreme Court of India (Article 32)",
            "High Courts of India (Article 226)",
            "National Human Rights Commission (NHRC)",
            "State Human Rights Commission (SHRC)"
        ],
        "important_documents": [
            "Constitution of India, Part III",
            "Proof of arbitrary or discriminatory state action",
            "Correspondence with public authorities"
        ],
        "official_sources": [
            {
                "source_type": "Constitutional Text",
                "source_name": "Constitution of India, Articles 14 to 32",
                "legal_section": "Part III (Fundamental Rights)",
                "last_verified": "Constitutional Law Reference",
                "verification_note": "Governed by the Supreme Court of India constitutional bench precedents."
            }
        ]
    },
    {
        "id": "labour-rights",
        "title": "Labour & Worker Rights",
        "title_tamil": "தொழிலாளர் மற்றும் பணியாளர் உரிமைகள்",
        "icon": "Briefcase",
        "badge": "Wages & Safety",
        "short_desc": "Rights regarding timely wage payment, minimum wage, working hours, gratuity, and protection from arbitrary termination.",
        "short_desc_tamil": "சரியான நேரத்தில் ஊதியம் பெறுதல், குறைந்தபட்ச ஊதியம், பணி நேரம், பணிக்கொடை மற்றும் நியாயமற்ற பணிநீக்கத்திற்கு எதிரான உரிமைகள்.",
        "overview": "Workers in India are protected under statutory enactments including the Payment of Wages Act 1936, Minimum Wages Act 1948, Industrial Disputes Act 1947, and Code on Wages. Employers cannot withhold legitimately earned wages, deny gratuity, or force hazardous work without statutory protections.",
        "overview_tamil": "இந்தியாவில் தொழிலாளர்கள் ஊதிய பட்டுவாடா சட்டம் 1936, குறைந்தபட்ச ஊதிய சட்டம் 1948 மற்றும் தொழிற்தகராறுகள் சட்டம் மூலம் பாதுகாக்கப்படுகிறார்கள். பணியாளரின் உழைப்புக்கான ஊதியத்தை நிறுத்தி வைக்கவோ, பணிக்கொடையை மறுக்கவோ சட்டப்படி முதலாளிக்கு உரிமையில்லை.",
        "common_questions": [
            {
                "q": "What should I do if my employer does not pay my salary?",
                "q_ta": "எனக்கு சம்பளம் கொடுக்கவில்லை என்றால் என்ன செய்ய வேண்டும்?",
                "a": "1. Issue a formal written demand/legal notice citing your employment contract. 2. File an online grievance on the Ministry of Labour Samadhan Portal (samadhan.labour.gov.in). 3. File a claim before the Labour Commissioner under Section 15 of Payment of Wages Act.",
                "a_ta": "1. நிறுவனத்திற்கு முறைப்படி கடிதம் அல்லது வக்கீல் நோட்டீஸ் அனுப்பவும். 2. மத்திய தொழிலாளர் அமைச்சகத்தின் சமாதான் போர்ட்டலில் (samadhan.labour.gov.in) புகார் அளிக்கவும். 3. தொழிலாளர் ஆணையரிடம் (Labour Commissioner) சட்டப்படி ஊதிய மீட்பு மனு தாக்கல் செய்யவும்."
            },
            {
                "q": "Can my employer seize my original educational certificates?",
                "q_ta": "நிறுவனம் எனது அசல் சான்றிதழ்களை பறிமுதல் செய்யலாமா?",
                "a": "No. Holding original personal certificates is illegal under Indian law and Department of Personnel & Training (DoPT) guidelines. Employers may only verify originals and keep photocopies.",
                "a_ta": "கூடாது. பணியாளரின் அசல் கல்வி சான்றிதழ்களை முதலாளி தன்வசம் வைத்துக்கொள்வது சட்டவிரோதமானது. சரிபார்க்க மட்டுமே அசல் கேட்கலாம், நகல்களை மட்டுமே வைத்துக்கொள்ள வேண்டும்."
            }
        ],
        "citizen_actions": [
            "Gather payslips, offer letter, bank statements, appointment letters, and attendance logs.",
            "Send an email with a 7 to 15-day deadline demanding salary disbursement.",
            "Lodge a conciliation petition with the jurisdictional Labour Officer.",
            "Contact National Career Service or e-Shram grievance support."
        ],
        "citizen_actions_tamil": [
            "சம்பள சீட்டு, பணி நியமன ஆணை, வங்கி அறிக்கை மற்றும் வருகைப் பதிவுகளை சேகரிக்கவும்.",
            "7 முதல் 15 நாட்களுக்குள் நிலுவை தொகையை செலுத்தக் கோரி முறையான மின்னஞ்சல் அனுப்பவும்.",
            "வட்டார தொழிலாளர் நல அலுவலரிடம் (Labour Officer) சமரச மனு தாக்கல் செய்யவும்.",
            "இ-ஷ்ராம் மற்றும் தேசிய தொழில் சேவை மையத்தின் உதவி பெறவும்."
        ],
        "relevant_authorities": [
            "Office of the Labour Commissioner (State & Central)",
            "Labour Court / Industrial Tribunal",
            "Employees' Provident Fund Organisation (EPFO)",
            "Employees' State Insurance Corporation (ESIC)"
        ],
        "important_documents": [
            "Employment Contract / Offer Letter",
            "Bank account statement showing missing deposits",
            "Past payslips & Form 16",
            "Written correspondence or email trail"
        ],
        "official_sources": [
            {
                "source_type": "Statutory Act",
                "source_name": "Payment of Wages Act, 1936",
                "legal_section": "Sections 5, 7, 15",
                "last_verified": "Ministry of Labour & Employment",
                "verification_note": "Governs statutory deadlines for wage disbursement (before 7th or 10th of every month)."
            }
        ]
    },
    {
        "id": "consumer-rights",
        "title": "Consumer Rights",
        "title_tamil": "நுகர்வோர் உரிமைகள்",
        "icon": "ShoppingCart",
        "badge": "Act 2019",
        "short_desc": "Protection against defective goods, deficient services, misleading advertisements, and unfair trade practices.",
        "short_desc_tamil": "தரமற்ற பொருட்கள், சேவைக் குறைபாடு, ஏமாற்று விளம்பரங்கள் மற்றும் நியாயமற்ற வர்த்தகத்திற்கு எதிரான பாதுகாப்பு.",
        "overview": "Under the Consumer Protection Act, 2019, consumers have the right to safety, information, choice, representation, redressal, and consumer education. Disputes can now be filed seamlessly online via the e-Daakhil portal without mandatory advocate representation.",
        "overview_tamil": "நுகர்வோர் பாதுகாப்பு சட்டம் 2019 இன் கீழ், தரமான பொருட்கள் மற்றும் குறைபாடற்ற சேவைகளைப் பெறுவது நுகர்வோரின் அடிப்படை உரிமை. பாதிக்கப்பட்டவர்கள் e-Daakhil இணையதளம் வழியாக வழக்கறிஞர் இன்றியே நேரடியாக நிவாரணம் கோரி வழக்கு தொடரலாம்.",
        "common_questions": [
            {
                "q": "How can I file a consumer complaint for a defective product?",
                "q_ta": "பழுதடைந்த பொருளுக்கு நுகர்வோர் புகார் அளிப்பது எப்படி?",
                "a": "Call the National Consumer Helpline at 1915 or register online at consumerhelpline.gov.in. If unresolved, file an e-complaint on the e-Daakhil portal (edaakhil.nic.in) before the District Consumer Commission.",
                "a_ta": "தேசிய நுகர்வோர் உதவி எண் 1915-ஐ அழைக்கலாம் அல்லது consumerhelpline.gov.in இணையத்தில் பதிவு செய்யலாம். தீர்வு கிடைக்காவிடில் edaakhil.nic.in மூலம் மாவட்ட நுகர்வோர் நீதிமன்றத்தில் வழக்கு தொடரலாம்."
            },
            {
                "q": "Can a shop charge more than the Maximum Retail Price (MRP)?",
                "q_ta": "கடையில் அச்சிடப்பட்ட விலையை (MRP) விட கூடுதல் கட்டணம் வசூலிக்கலாமா?",
                "a": "Charging above MRP is illegal under the Legal Metrology Act and Consumer Protection Act. You can file a grievance with the Legal Metrology Department and National Consumer Helpline.",
                "a_ta": "சட்டப்படி MRP விலையை விட ஒரு ரூபாய் கூட அதிகம் வசூலிக்கக் கூடாது. இது தண்டனைக்குரிய குற்றம். நுகர்வோர் உதவி எண் 1915-ல் உடனடி புகார் அளிக்கலாம்."
            }
        ],
        "citizen_actions": [
            "Preserve original invoice, tax bill, warranty card, and digital payment receipts.",
            "Record photographic/video evidence of defects or substandard service.",
            "Send a written grievance to the customer support and grievance officer of the company.",
            "Call National Consumer Helpline (NCH) 1915 for pre-litigation resolution."
        ],
        "citizen_actions_tamil": [
            "அசல் ரசீது, பில், வாரண்டி அட்டை மற்றும் பரிவர்த்தனை ஆதாரங்களை பாதுகாக்கவும்.",
            "பொருளின் குறைபாட்டை வீடியோ அல்லது புகைப்பட ஆதாரமாக பதிவு செய்யவும்.",
            "நிறுவனத்தின் குறைதீர்க்கும் அதிகாரிக்கு மின்னஞ்சல் அனுப்பவும்.",
            "தேசிய நுகர்வோர் உதவி எண் 1915-ஐ தொடர்பு கொண்டு வழிகாட்டுதல் பெறவும்."
        ],
        "relevant_authorities": [
            "National Consumer Helpline (Dept of Consumer Affairs)",
            "District Consumer Disputes Redressal Commission (DCDRC)",
            "Central Consumer Protection Authority (CCPA)",
            "Legal Metrology Department"
        ],
        "important_documents": [
            "Retail Bill / GST Invoice",
            "Warranty Card / Service Agreement",
            "Email communication with merchant",
            "Photographs / Delivery unboxing video"
        ],
        "official_sources": [
            {
                "source_type": "Statutory Act",
                "source_name": "Consumer Protection Act, 2019",
                "legal_section": "Section 2(7), Section 35",
                "last_verified": "Ministry of Consumer Affairs",
                "verification_note": "Establishes Consumer Commissions and online filing via e-Daakhil."
            }
        ]
    },
    {
        "id": "police-legal-rights",
        "title": "Police & Legal Rights",
        "title_tamil": "காவல்துறை மற்றும் சட்ட உரிமைகள்",
        "icon": "ShieldAlert",
        "badge": "CrPC & BNSS",
        "short_desc": "Rights during police questioning, search, arrest procedures, FIR registration, and bail entitlements.",
        "short_desc_tamil": "காவல்துறை விசாரணை, தேடுதல், கைது நடைமுறைகள், முதல் தகவல் அறிக்கை (FIR) மற்றும் ஜாமீன் உரிமைகள்.",
        "overview": "Every citizen has defined constitutional and statutory protections against arbitrary detention, custodial violence, and unlawful arrest under Articles 20, 21, 22 of the Constitution and the Code of Criminal Procedure (CrPC) / Bharatiya Nagarik Suraksha Sanhita (BNSS). Supreme Court D.K. Basu guidelines mandate clear protocols for police personnel.",
        "overview_tamil": "அரசியலமைப்பு பிரிவுகள் 20, 21, 22 மற்றும் குற்றவியல் நடைமுறைச் சட்டத்தின் கீழ் அத்துமீறிய கைது மற்றும் காவல் துன்புறுத்தல்களுக்கு எதிராக குடிமக்களுக்கு முழு உரிமை உண்டு. உச்ச நீதிமன்றத்தின் டி.கே. பாசு வழிகாட்டுதல்கள் காவல்துறை பின்பற்ற வேண்டிய கட்டாய நெறிமுறைகளை வகுத்துள்ளன.",
        "common_questions": [
            {
                "q": "What are my rights if I am stopped or arrested by the police?",
                "q_ta": "போலீஸ் என்னை தடுத்தால் அல்லது கைது செய்தால் எனக்கு என்ன உரிமைகள் உள்ளன?",
                "a": "1. Right to know the exact grounds of arrest. 2. Police must prepare an Arrest Memo signed by a witness. 3. Right to inform a friend or relative. 4. Right to consult an advocate of your choice. 5. Must be produced before a Magistrate within 24 hours. 6. Right to free medical examination.",
                "a_ta": "1. கைதுக்கான காரணத்தை உடனடியாக அறிந்து கொள்ளும் உரிமை. 2. கைது ஆவணம் (Arrest Memo) தயாரித்து சாட்சி கையெழுத்து பெற வேண்டும். 3. குடும்பத்தினர் அல்லது நண்பருக்கு தகவல் தெரிவிக்கும் உரிமை. 4. வழக்கறிஞரை சந்திக்கும் உரிமை. 5. 24 மணி நேரத்திற்குள் மாஜிஸ்திரேட் முன் ஆஜர்படுத்தப்பட வேண்டும்."
            },
            {
                "q": "Can women be arrested at night?",
                "q_ta": "பெண்களை இரவில் கைது செய்யலாமா?",
                "a": "Section 46(4) of CrPC mandates that no woman shall be arrested after sunset and before sunrise, except in extraordinary circumstances with prior written permission of a Judicial Magistrate, and only in the presence of a female police officer.",
                "a_ta": "CrPC பிரிவு 46(4) இன் படி, சூரிய அஸ்தமனத்திற்குப் பிறகும், சூரிய உதயத்திற்கு முன்பும் பெண்களை கைது செய்யக்கூடாது. தவிர்க்க முடியாத சூழலில் பெண் காவலர் முன்னிலையில் மாஜிஸ்திரேட்டின் முன் அனுமதி பெற்றே கைது செய்ய முடியும்."
            }
        ],
        "citizen_actions": [
            "Politely request the officer's name, badge number, and designated police station.",
            "Ask clearly whether you are being arrested or merely asked to assist with an inquiry.",
            "Request preparation of an Arrest Memo with the exact time, date, and location.",
            "Do not sign blank papers; insist on immediate access to a legal representative.",
            "Contact District Legal Services Authority (DLSA) for free government legal aid."
        ],
        "citizen_actions_tamil": [
            "காவலரின் பெயர், பேட்ஜ் எண் மற்றும் காவல் நிலையத்தை கண்ணியமாக கேட்டு அறியவும்.",
            "விசாரணைக்கா அல்லது கைதா என்பதை தெளிவாகக் கேட்கவும்.",
            "கைது செய்யப்பட்டால் முறையான Arrest Memo வழங்க வலியுறுத்தவும்.",
            "வெற்றுத் தாள்களில் கையெழுத்திட மறுக்கவும்; உடனடியாக வழக்கறிஞரை தொடர்பு கொள்ள உரிமை கோரவும்.",
            "இலவச அரசு சட்ட உதவிக்கு மாவட்ட சட்டப் பணிகள் ஆணைக்குழுவை (DLSA) அணுகலாம்."
        ],
        "relevant_authorities": [
            "Jurisdictional Judicial Magistrate Court",
            "District Legal Services Authority (DLSA / NALSA Helpline 15100)",
            "Police Complaints Authority (PCA)",
            "State Human Rights Commission"
        ],
        "important_documents": [
            "Copy of FIR (Free copy is mandatory under law)",
            "Arrest Memo / Inspection Memo",
            "Medical Examination Report",
            "Identity Proof"
        ],
        "official_sources": [
            {
                "source_type": "Supreme Court Landmark Ruling",
                "source_name": "D.K. Basu v. State of West Bengal (1997)",
                "legal_section": "11 Mandatory Directives on Arrest & Custody",
                "last_verified": "Supreme Court of India",
                "verification_note": "Binding across all states and police departments in India."
            }
        ]
    },
    {
        "id": "digital-privacy-rights",
        "title": "Digital & Privacy Rights",
        "title_tamil": "டிஜிட்டல் மற்றும் தனியுரிமை",
        "icon": "Lock",
        "badge": "DPDP & IT Act",
        "short_desc": "Rights against unauthorized surveillance, data misuse, identity theft, financial cyber fraud, and online stalking.",
        "short_desc_tamil": "অনலைனில் தனியுரிமை பாதுகாப்பு, வங்கி ஆன்லைன் மோசடி, தரவு தவறாக பயன்படுத்துதல் மற்றும் சைபர் குற்றங்களுக்கு எதிரான உரிமைகள்.",
        "overview": "The Right to Privacy is a Fundamental Right under Article 21 (Puttaswamy landmark judgment). Citizens are protected under the Information Technology Act 2000 and Digital Personal Data Protection (DPDP) Act against identity theft, cyberstalking, financial fraud, and unauthorized corporate tracking.",
        "overview_tamil": "புட்டாசாமி தீர்ப்பின்படி தனிமனித ரகசிய காப்புரிமை (Privacy) அடிப்படை உரிமையாகும். ஐடி சட்டம் மற்றும் டிஜிட்டல் தனிநபர் தரவு பாதுகாப்பு சட்டம் குடிமக்களின் இணைய பாதுகாப்பு மற்றும் வங்கி மோசடிகளுக்கு எதிராக வலுவான உரிமைகளை வழங்குகிறது.",
        "common_questions": [
            {
                "q": "What should I do immediately if I lose money in an online UPI / banking fraud?",
                "q_ta": "ஆன்லைன் வங்கி அல்லது UPI மோசடியில் பணம் போனால் உடனடியாக என்ன செய்ய வேண்டும்?",
                "a": "Act in the 'Golden Hour'! Call 1930 Cyber Fraud Helpline immediately. Block your card/UPI via your bank mobile app. Lodge a complaint on cybercrime.gov.in within 24 hours to help freeze the recipient's bank account.",
                "a_ta": "முதல் 2 மணி நேரம் மிகவும் முக்கியம் ('Golden Hour')! உடனடியாக 1930 சைபர் உதவி எண்ணை அழைக்கவும். உங்கள் வங்கி செயலியில் கார்டு/UPI-ஐ முடக்கவும். cybercrime.gov.in போர்ட்டலில் புகார் பதிவு செய்து பணத்தை முடக்க நடவடிக்கை எடுக்கவும்."
            },
            {
                "q": "Can loan recovery apps access my phone contacts or harass my contacts?",
                "q_ta": "கடன் செயலிகள் எனது மொபைல் தொடர்புகளை திருடி மிரட்டலாமா?",
                "a": "No. RBI guidelines strictly prohibit loan aggregators and NBFC recovery agents from accessing personal media/contacts or harassing borrowers. Report to sachet.rbi.org.in and cyber police.",
                "a_ta": "கூடாது. ரிசர்வ் வங்கியின் (RBI) விதிமுறைகளின்படி எந்த கடன் செயலியும் போன் தொடர்புகளை அணுகவோ, நண்பர்களுக்கு போன் செய்து அச்சுறுத்தவோ அனுமதி இல்லை. RBI Sachet போர்ட்டலில் புகார் அளிக்கலாம்."
            }
        ],
        "citizen_actions": [
            "Capture screenshots of fraudulent SMS, transaction UTR numbers, payment links, and call logs.",
            "Call the 1930 National Cybercrime helpline within minutes of unauthorized debit.",
            "Instruct your bank to initiate a chargeback and freeze the beneficiary account.",
            "Register an acknowledgement number at national portal cybercrime.gov.in."
        ],
        "citizen_actions_tamil": [
            "மோசடி குறுஞ்செய்தி, வங்கி பரிவர்த்தனை எண் (UTR) மற்றும் போன் அழைப்புகளை ஸ்கிரீன்ஷாட் எடுக்கவும்.",
            "பணம் இழந்தவுடன் உடனடியாக 1930 தேசிய சைபர் உதவி எண்ணை அழைக்கவும்.",
            "வங்கியிடம் தெரிவித்து அந்த பணப் பரிவர்த்தனையை திரும்பப் பெற (Chargeback) கோரிக்கை வைக்கவும்.",
            "cybercrime.gov.in இணையத்தில் முழு விவரங்களுடன் அதிகாரப்பூர்வ புகார் பதிவு செய்யவும்."
        ],
        "relevant_authorities": [
            "National Cyber Crime Reporting Portal (MHA)",
            "Cyber Helpline 1930",
            "Reserve Bank of India (RBI Banking Ombudsman)",
            "Data Protection Board of India"
        ],
        "important_documents": [
            "Bank account mini statement showing fraudulent debit",
            "Transaction IDs / UPI Reference Number (UTR)",
            "Screenshots of phishing messages or suspicious links",
            "Call records and sender phone numbers"
        ],
        "official_sources": [
            {
                "source_type": "Statutory Act",
                "source_name": "Information Technology Act, 2000",
                "legal_section": "Sections 43, 66C, 66D",
                "last_verified": "Ministry of Electronics and Information Technology",
                "verification_note": "Prescribes penalties for cyber fraud, phishing, and identity theft."
            }
        ]
    },
    {
        "id": "women-child-rights",
        "title": "Women & Child Rights",
        "title_tamil": "பெண்கள் மற்றும் குழந்தைகள் உரிமைகள்",
        "icon": "HeartHandshake",
        "badge": "POSH & DV Act",
        "short_desc": "Protections under Domestic Violence Act, POSH Act against workplace sexual harassment, and POCSO.",
        "short_desc_tamil": "குடும்ப வன்முறை தடுப்புச் சட்டம், பணியிட பாலியல் துன்புறுத்தல் தடுப்புச் சட்டம் (POSH) மற்றும் போக்சோ பாதுகாப்பு.",
        "overview": "Indian laws offer comprehensive protections against gender-based violence and child exploitation. Key enactments include the Protection of Women from Domestic Violence Act 2005, Sexual Harassment of Women at Workplace (POSH) Act 2013, and POCSO Act 2012.",
        "overview_tamil": "பெண்கள் மற்றும் குழந்தைகளுக்கு எதிரான வன்முறைகளைத் தடுக்க இந்தியாவில் வலுவான சட்டங்கள் உள்ளன. குடும்ப வன்முறை தடுப்புச் சட்டம் 2005, பணியிட பாலியல் புகார் தடுப்புச் சட்டம் (POSH) மற்றும் போக்சோ சட்டம் மூலம் உடனடி பாதுகாப்பு மற்றும் நிவாரணம் பெறலாம்.",
        "common_questions": [
            {
                "q": "What is the procedure for reporting workplace harassment under the POSH Act?",
                "q_ta": "வேலை செய்யும் இடத்தில் பாலியல் தொல்லை ஏற்பட்டால் POSH சட்டப்படி புகார் செய்வது எப்படி?",
                "a": "Submit a written complaint to your employer's Internal Committee (IC) within 3 months of the incident. If no IC exists or the employer fails to act, complaint can be filed with the District Local Committee or through the SHe-Box portal.",
                "a_ta": "சம்பவம் நடந்த 3 மாதங்களுக்குள் நிறுவனத்தின் உள் புகார் குழுவிடம் (Internal Committee - IC) எழுத்துப்பூர்வ புகார் அளிக்க வேண்டும். குழு இல்லாதபட்சத்தில் மாவட்டக் குழு அல்லது மத்திய அரசின் SHe-Box இணையத்தில் புகார் அளிக்கலாம்."
            },
            {
                "q": "Where can a woman get immediate shelter and legal protection from domestic violence?",
                "q_ta": "குடும்ப வன்முறையால் பாதிக்கப்பட்ட பெண் உடனடி அடைக்கலம் மற்றும் சட்ட உதவி பெற எங்கு செல்ல வேண்டும்?",
                "a": "Call the Women Helpline 181 or 1091. You can approach a Protection Officer appointed by the State Government, One Stop Centre (Sakhi Centre), or approach the Magistrate under Section 12 of the Domestic Violence Act.",
                "a_ta": "பெண்கள் உதவி எண் 181 அல்லது 1091-ஐ அழைக்கவும். அரசு நியமித்துள்ள பாதுகாப்பு அலுவலர் (Protection Officer), 'சகி' ஆதரவு மையம் அல்லது மாஜிஸ்திரேட்டை அணுகி உடனடி பாதுகாப்பு ஆணை பெறலாம்."
            }
        ],
        "citizen_actions": [
            "Call 181 (Women Helpline) or 1098 (Childline) for confidential immediate rescue.",
            "Preserve any text messages, emails, photos, or witness accounts.",
            "Approach the nearest One Stop Centre (Sakhi Centre) for medical, legal, and counseling help.",
            "Lodge an e-complaint on the National Commission for Women (NCW) portal."
        ],
        "citizen_actions_tamil": [
            "ரகசிய அவசர உதவிக்கு 181 (பெண்கள்) அல்லது 1098 (குழந்தைகள்) எண்ணை தொடர்பு கொள்ளவும்.",
            "குறுஞ்செய்தி, புகைப்படங்கள் மற்றும் சாட்சிகளின் விவரங்களை பாதுகாப்பாக வைக்கவும்.",
            "மருத்துவ, சட்ட மற்றும் மனநல உதவிக்கு அரசு 'சகி' (One Stop Centre) மையத்தை அணுகவும்.",
            "தேசிய மகளிர் ஆணையத்தின் (NCW) இணையதளத்தில் ஆன்லைன் புகார் பதிவு செய்யலாம்."
        ],
        "relevant_authorities": [
            "National Commission for Women (NCW)",
            "State Women Commission",
            "One Stop Centre (Sakhi Centres)",
            "District Child Protection Unit (DCPU)"
        ],
        "important_documents": [
            "Chronological diary of events or incidents",
            "Medical certificates in case of physical injury",
            "Digital records of threatening calls or texts"
        ],
        "official_sources": [
            {
                "source_type": "Statutory Act",
                "source_name": "Protection of Women from Domestic Violence Act, 2005",
                "legal_section": "Sections 12, 18, 19 (Protection and Residence Orders)",
                "last_verified": "Ministry of Women and Child Development",
                "verification_note": "Grants emergency residence orders and financial maintenance."
            }
        ]
    },
    {
        "id": "rti-transparency",
        "title": "Government Transparency & RTI",
        "title_tamil": "தகவல் அறியும் உரிமைச் சட்டம் (RTI)",
        "icon": "FileText",
        "badge": "RTI Act 2005",
        "short_desc": "Right to inspect government records, tenders, fund allocations, and public service files within 30 days.",
        "short_desc_tamil": "அரசு கோப்புகள், திட்ட நிதி செலவுகள் மற்றும் பொது சேவை நிலைகளை 30 நாட்களில் தெரிந்து கொள்ளும் உரிமை.",
        "overview": "The Right to Information Act, 2005 empowers Indian citizens to question public authorities, demand copies of official files, verify muster rolls, and inspect public works. Public Information Officers (PIOs) are legally mandated to reply within 30 days (or 48 hours for life and liberty).",
        "overview_tamil": "தகவல் அறியும் உரிமைச் சட்டம் 2005 குடிமக்களுக்கு அரசு ஆவணங்களை ஆய்வு செய்யவும், அரசு நிதி எவ்வாறு செலவிடப்படுகிறது என்பதை அறியவும் அதிகாரம் அளிக்கிறது. அரசு பொதுத் தகவல் அலுவலர் 30 நாட்களுக்குள் தகவல் அளிக்க வேண்டும்.",
        "common_questions": [
            {
                "q": "How do I file an RTI application?",
                "q_ta": "RTI மூலம் அரசு அலுவலகத்தில் தகவல் கேட்பது எப்படி?",
                "a": "For Central departments, apply online at rtionline.gov.in with a Rs 10 fee. For state authorities, submit a written or typed application to the Public Information Officer (PIO) via speed post or state RTI portal.",
                "a_ta": "மத்திய அரசு துறைகளுக்கு rtionline.gov.in மூலம் ரூ.10 கட்டணம் செலுத்தி விண்ணப்பிக்கலாம். மாநில அரசு துறைகளுக்கு உரிய பொதுத் தகவல் அலுவலருக்கு (PIO) தபாலில் அல்லது மாநில RTI இணையத்தில் விண்ணப்பிக்கலாம்."
            },
            {
                "q": "What if the government officer refuses or fails to reply within 30 days?",
                "q_ta": "அதிகாரி 30 நாட்களில் தகவல் தரவில்லை என்றால் என்ன செய்வது?",
                "a": "File a 'First Appeal' under Section 19(1) to the designated First Appellate Authority within 30 days. If still dissatisfied, file a 'Second Appeal' before the Central or State Information Commission.",
                "a_ta": "பிரிவு 19(1) இன் கீழ் 30 நாட்களுக்குள் மேல்முறையீட்டு அலுவலரிடம் 'முதல் மேல்முறையீடு' செய்யலாம். அதிலும் திருப்தியில்லை என்றால் மாநில அல்லது மத்திய தகவல் ஆணையத்தில் புகார் செய்யலாம்."
            }
        ],
        "citizen_actions": [
            "Identify the exact public department holding the information.",
            "Draft concise, specific questions asking for existing records, not opinions or hypothetical answers.",
            "Pay the statutory application fee of Rs 10 (exempt for BPL cardholders).",
            "Note the tracking number and calculate the 30-day statutory response clock."
        ],
        "citizen_actions_tamil": [
            "தகவல் எந்த அரசு துறையிடம் உள்ளது என்பதை துல்லியமாக கண்டறியவும்.",
            "கருத்துக்கள் கேட்காமல், ஆவணங்களின் நகல்களை மட்டுமே தெளிவாகக் குறிப்பிட்டு கேட்கவும்.",
            "ரூபாய் 10 விண்ணப்பக் கட்டணம் செலுத்தவும் (வறுமைக் கோட்டிற்கு கீழ் உள்ளவர்களுக்கு கட்டணம் இல்லை).",
            "விண்ணப்பித்த தேதியை குறித்து வைத்து 30 நாள் காலக்கெடுவை கண்காணிக்கவும்."
        ],
        "relevant_authorities": [
            "Public Information Officer (PIO) of respective department",
            "First Appellate Authority (FAA)",
            "Central Information Commission (CIC)",
            "State Information Commission (SIC)"
        ],
        "important_documents": [
            "Formal RTI application letter",
            "Postal Order / Online Payment Receipt (Rs 10)",
            "Proof of delivery (India Post tracking slip)"
        ],
        "official_sources": [
            {
                "source_type": "Statutory Act",
                "source_name": "Right to Information Act, 2005",
                "legal_section": "Sections 6, 7, 19",
                "last_verified": "Department of Personnel and Training (DoPT)",
                "verification_note": "Governs statutory timelines and penalties up to Rs 25,000 on defaulting officers."
            }
        ]
    },
    {
        "id": "education-rights",
        "title": "Education Rights",
        "title_tamil": "கல்வி உரிமைகள்",
        "icon": "GraduationCap",
        "badge": "RTE Act 2009",
        "short_desc": "Free and compulsory education for children aged 6 to 14, 25% EWS reservation in private schools, anti-ragging protections.",
        "short_desc_tamil": "6 முதல் 14 வயது வரை இலவச மற்றும் கட்டாயக் கல்வி, தனியார் பள்ளிகளில் 25% ஏழை எளியோர் இடஒதுக்கீடு, கேலி வதை தடுப்பு.",
        "overview": "Article 21A of the Constitution and the Right of Children to Free and Compulsory Education (RTE) Act 2009 ensure that every child has a right to quality basic education. Under Section 12(1)(c), private un-aided schools must reserve 25% seats for disadvantaged groups with fee reimbursement by the government.",
        "overview_tamil": "அரசியலமைப்பு பிரிவு 21A மற்றும் இலவச கட்டாய கல்வி உரிமைச் சட்டம் 2009 ஒவ்வொரு குழந்தைக்கும் கல்வி அடிப்படை உரிமை என கூறுகிறது. தனியார் பள்ளிகளில் 25% இடங்கள் ஏழை எளிய குடும்பங்களைச் சேர்ந்த குழந்தைகளுக்கு இலவசமாக ஒதுக்கப்பட வேண்டும்.",
        "common_questions": [
            {
                "q": "How can I apply for 25% free school admission under RTE?",
                "q_ta": "RTE சட்டத்தின் கீழ் தனியார் பள்ளியில் 25% இலவச சேர்க்கை பெறுவது எப்படி?",
                "a": "State governments conduct an annual online RTE admission lottery portal (e.g. rte.tnschools.gov.in in TN). Parents from EWS (income below state limit) and disadvantaged groups can apply with birth & income proof.",
                "a_ta": "மாநில கல்வித்துறையின் RTE இணையதளம் மூலம் ஆண்டுதோறும் விண்ணப்பங்கள் பெறப்படுகின்றன. வருமானச் சான்றிதழ் மற்றும் இருப்பிடச் சான்றிதழ் சமர்ப்பித்து ஆன்லைனில் இலவச சேர்க்கைக்கு விண்ணப்பிக்கலாம்."
            },
            {
                "q": "What should a college student do if facing ragging?",
                "q_ta": "கல்லூரியில் ராகிங் (Ragging) தொல்லை ஏற்பட்டால் என்ன செய்ய வேண்டும்?",
                "a": "Dial the 24x7 National Anti-Ragging Helpline 1800-180-5522 or email helpline@antiragging.in. Ragging is a cognizable criminal offense punishable under UGC regulations and IPC/BNS.",
                "a_ta": "தேசிய ராகிங் எதிர்ப்பு இலவச உதவி எண் 1800-180-5522 ஐ அழைக்கவும். ராகிங் செய்வது தண்டனைக்குரிய குற்றமாகும். கல்லூரி நிர்வாகம் மற்றும் காவல் நிலையத்தில் உடனடியாக புகார் அளிக்கலாம்."
            }
        ],
        "citizen_actions": [
            "Check the state RTE admission notification calendar (usually Feb - April each year).",
            "Collect Income Certificate, Child Birth Certificate, and Community Certificate.",
            "Report capitation fee or screening interview demands to the District Education Officer (DEO).",
            "Contact National Commission for Protection of Child Rights (NCPCR) for RTE violations."
        ],
        "citizen_actions_tamil": [
            "ஆண்டுதோறும் கல்வித்துறை வெளியிடும் RTE அறிவிப்பு தேதிகளை கவனிக்கவும்.",
            "வருமானச் சான்று, பிறப்புச் சான்று மற்றும் இருப்பிடச் சான்றுகளை தயார் செய்து வைக்கவும்.",
            "தனியார் பள்ளிகள் நன்கொடை அல்லது நுழைவுத்தேர்வு கட்டாயப்படுத்தினால் கல்வி அலுவலரிடம் புகார் செய்யவும்.",
            "மீறல்கள் குறித்து தேசிய குழந்தைகள் உரிமைகள் பாதுகாப்பு ஆணையத்தில் (NCPCR) புகார் செய்யலாம்."
        ],
        "relevant_authorities": [
            "District Educational Officer (DEO) / Chief Educational Officer (CEO)",
            "National Commission for Protection of Child Rights (NCPCR)",
            "University Grants Commission (UGC Anti-Ragging Cell)"
        ],
        "important_documents": [
            "Child's Birth Certificate",
            "Income Certificate issued by Revenue Authority (Tahsildar)",
            "Address proof (Aadhaar, Ration card)",
            "Community Certificate (if applicable)"
        ],
        "official_sources": [
            {
                "source_type": "Statutory Act",
                "source_name": "Right of Children to Free and Compulsory Education Act, 2009",
                "legal_section": "Section 12(1)(c)",
                "last_verified": "Ministry of Education",
                "verification_note": "Mandates 25% reservation in entry-level classes in private schools."
            }
        ]
    },
    {
        "id": "healthcare-rights",
        "title": "Healthcare Rights",
        "title_tamil": "சுகாதார மற்றும் நோயாளி உரிமைகள்",
        "icon": "Activity",
        "badge": "Patient Charter",
        "short_desc": "Right to emergency medical treatment without upfront advance, informed consent, medical record copies, and price caps.",
        "short_desc_tamil": "முன்பணம் இன்றி அவசர சிகிச்சை பெறும் உரிமை, மருத்துவ ஆவண நகல்களைப் பெறுதல் மற்றும் சிகிச்சை கட்டண வெளிப்படைத்தன்மை.",
        "overview": "Under the Charter of Patients' Rights adopted by the National Human Rights Commission (NHRC) and Ministry of Health, every patient has the right to emergency medical care without commercial delay, right to confidentiality, right to their medical records within 72 hours, and right to second opinion.",
        "overview_tamil": "மனித உரிமைகள் ஆணையத்தின் நோயாளி சாசனத்தின்படி, விபத்து அல்லது அவசர சிகிச்சையை முன்பணம் கேட்டு மறுக்க எந்த மருத்துவமனைக்கும் உரிமை இல்லை. சிகிச்சை ஆவணங்களை 72 மணி நேரத்திற்குள் நோயாளிக்கு வழங்குவது மருத்துவமனையின் சட்டப்பூர்வ கடமை.",
        "common_questions": [
            {
                "q": "Can a private hospital refuse emergency treatment if I cannot pay advance money?",
                "q_ta": "முன்பணம் செலுத்தவில்லை என்று தனியார் மருத்துவமனை அவசர சிகிச்சையை மறுக்கலாமா?",
                "a": "No. The Supreme Court in the landmark Parmanand Katara judgment ruled that preservation of human life is paramount. Every doctor and hospital is legally bound to provide immediate first aid and stabilization without waiting for police formalities or advance payment.",
                "a_ta": "கூடாது. உச்ச நீதிமன்ற தீர்ப்பின்படி மனித உயிரை காப்பதே முதன்மையானது. காவல் துறை விசாரணை அல்லது முன்பணம் கேட்காமல் முதலுதவி மற்றும் அவசர சிகிச்சை அளிப்பது அனைத்து மருத்துவமனைகளின் கட்டாய கடமையாகும்."
            },
            {
                "q": "Can a hospital detain a deceased body over unpaid medical bills?",
                "q_ta": "பில் பாக்கி செலுத்தவில்லை என்று மருத்துவமனை உடலை தடுத்து வைக்கலாமா?",
                "a": "No. Detaining a patient or a dead body for bill clearance is illegal and an offense violating human dignity under Article 21. You can immediately call police (112) or file a grievance with the State Clinical Establishments Authority.",
                "a_ta": "கண்டிப்பாக கூடாது. நிலுவை பணத்திற்காக உடலை ஒப்படைக்க மறுப்பது மனித கண்ணியத்தை மீறும் சட்டவிரோத செயலாகும். உடனடியாக 112 காவல்துறை உதவி எண்ணை அழைத்து புகார் தெரிவிக்கலாம்."
            }
        ],
        "citizen_actions": [
            "Request an itemized billing estimate before major non-emergency procedures.",
            "Ask in writing for copies of case sheets, lab reports, and discharge summary.",
            "Report hospital billing overcharging or negligence to the State Medical Council.",
            "Utilize PM-JAY / State Government Health Insurance schemes where empaneled."
        ],
        "citizen_actions_tamil": [
            "சிகிச்சை கட்டணத்திற்கான முழு விவர அறிக்கையை (Itemized Bill) கோரி பெறவும்.",
            "மருத்துவ பரிசோதனை அறிக்கைகள் மற்றும் டிஸ்சார்ஜ் சம்மரியை எழுத்துப்பூர்வமாக கேட்கவும்.",
            "மருத்துவ அலட்சியம் அல்லது கூடுதல் கட்டண வசூல் குறித்து மாநில மருத்துவ கவுன்சிலில் புகார் செய்யலாம்.",
            "அரசு மருத்துவ காப்பீட்டு திட்டங்களின் கீழ் உள்ள சிகிச்சைகளை சரிபார்க்கவும்."
        ],
        "relevant_authorities": [
            "National Medical Commission (NMC)",
            "State Medical Council",
            "State Clinical Establishment Regulatory Authority",
            "National Consumer Disputes Redressal Commission (Medical Negligence)"
        ],
        "important_documents": [
            "Hospital Admission & Discharge Summary",
            "Detailed itemized medical bill",
            "Investigation reports and doctor prescription slips"
        ],
        "official_sources": [
            {
                "source_type": "Supreme Court Landmark Judgment",
                "source_name": "Pt. Parmanand Katara v. Union of India (1989)",
                "legal_section": "Emergency Medical Care Right (Article 21)",
                "last_verified": "Supreme Court of India",
                "verification_note": "Establishes doctors' unconditional duty to administer emergency care."
            }
        ]
    },
    {
        "id": "environmental-rights",
        "title": "Environmental Rights",
        "title_tamil": "சுற்றுச்சூழல் உரிமைகள்",
        "icon": "Trees",
        "badge": "NGT & Art 21",
        "short_desc": "Right to clean air, safe drinking water, noise pollution restrictions, and filing petitions before National Green Tribunal.",
        "short_desc_tamil": "தூய்மையான காற்று, குடிநீர், ஒலி மாசு கட்டுப்பாடு மற்றும் தேசிய பசுமை தீர்ப்பாயத்தில் (NGT) வழக்கு தொடரும் உரிமை.",
        "overview": "The Supreme Court has consistently held that the Right to Life under Article 21 includes the right to a clean, healthy, and pollution-free environment. Citizens can file grievances regarding industrial waste, lake encroachment, or illegal groundwater depletion before the National Green Tribunal (NGT) and Pollution Control Boards.",
        "overview_tamil": "அரசியலமைப்பு பிரிவு 21-ன் படி தூய்மையான காற்று மற்றும் சுகாதாரமான சுற்றுச்சூழலில் வாழ்வது மக்களின் அடிப்படை உரிமை. நீர்நிலைகள் ஆக்கிரமிப்பு, தொழிற்சாலை கழிவுகள் மற்றும் ஒலி மாசு குறித்து தேசிய பசுமை தீர்ப்பாயத்தில் (NGT) முறையிடலாம்.",
        "common_questions": [
            {
                "q": "What are the rules regarding loud music / loudspeakers at night?",
                "q_ta": "இரவு நேரங்களில் அதிக சத்தத்துடன் ஸ்பீக்கர் பயன்படுத்துவதற்கு என்ன விதிகள் உள்ளன?",
                "a": "Under the Noise Pollution (Regulation and Control) Rules, 2000, loudspeakers are prohibited between 10:00 PM and 6:00 AM in public places without special permission. Dial 112 to report noise pollution.",
                "a_ta": "ஒலி மாசு கட்டுப்பாடு விதிகளின்படி இரவு 10 மணி முதல் காலை 6 மணி வரை பொது இடங்களில் ஒலிபெருக்கிகள் பயன்படுத்த அனுமதி இல்லை. 112 எண்ணை அழைத்து உடனடியாக புகார் தெரிவிக்கலாம்."
            },
            {
                "q": "Can a citizen file a case directly in the National Green Tribunal (NGT)?",
                "q_ta": "சுற்றுச்சூழல் பாதிப்புக்கு ஒரு சாதாரண குடிமகன் NGT தீர்ப்பாயத்தை அணுகலாமா?",
                "a": "Yes. Any aggrieved citizen can file an application or letter petition before the NGT against illegal tree felling, lake destruction, or industrial pollution under the NGT Act 2010.",
                "a_ta": "ஆம். நீர்நிலை ஆக்கிரமிப்பு, சட்டவிரோத மரம் வெட்டுதல் அல்லது காற்று/நீர் மாசு குறித்து எந்த குடிமகனும் தேசிய பசுமை தீர்ப்பாயத்தில் (NGT) நேரடியாக மனு தாக்கல் செய்யலாம்."
            }
        ],
        "citizen_actions": [
            "Record date, time, and geo-tagged photographic evidence of pollution or illegal dumping.",
            "Lodge an online complaint on the State Pollution Control Board portal.",
            "Call local municipal health department or police (112) for nighttime noise violations.",
            "File an original application before the Principal Bench or Zonal Bench of the NGT."
        ],
        "citizen_actions_tamil": [
            "மாசு அல்லது குப்பை எரித்தல் நடக்கும் இடத்தின் புகைப்படம் மற்றும் நேரத்தை பதிவு செய்யவும்.",
            "மாநில மாசு கட்டுப்பாட்டு வாரிய இணையதளத்தில் புகார் அளிக்கவும்.",
            "இரவு நேர ஒலி மாசு குறித்து 112 போலீஸ் உதவி எண்ணில் தகவல் தெரிவிக்கவும்.",
            "பசுமை தீர்ப்பாயத்தில் மனு தாக்கல் செய்து பொது ஆதாரங்களை சமர்ப்பிக்கவும்."
        ],
        "relevant_authorities": [
            "National Green Tribunal (NGT)",
            "Central Pollution Control Board (CPCB)",
            "State Pollution Control Board (SPCB)",
            "Local Municipal Corporation / Panchayat"
        ],
        "important_documents": [
            "Geo-tagged photographs/video of dumping or effluent discharge",
            "Water test reports from certified laboratories",
            "Written complaint copies acknowledged by local authorities"
        ],
        "official_sources": [
            {
                "source_type": "Statutory Act",
                "source_name": "National Green Tribunal Act, 2010",
                "legal_section": "Sections 14, 15",
                "last_verified": "Ministry of Environment, Forest and Climate Change",
                "verification_note": "Governs judicial remedy for environmental damage and restoration."
            }
        ]
    }
]

def get_all_categories():
    return RIGHTS_CATEGORIES

def get_category_by_id(cat_id: str):
    for cat in RIGHTS_CATEGORIES:
        if cat["id"] == cat_id:
            return cat
    return None
