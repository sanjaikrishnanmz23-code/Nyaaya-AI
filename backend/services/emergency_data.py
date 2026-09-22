"""
Verified Indian Citizen Emergency Helplines Matrix
Official public numbers with clear educational labeling and bilingual descriptions.
"""

EMERGENCY_CONTACTS = [
    {
        "id": "national-emergency",
        "name": "Single Emergency Helpline (ERSS)",
        "name_tamil": "ஒற்றை அவசர உதவி எண் (காவல்/தீயணைப்பு/ஆம்புலன்ஸ்)",
        "number": "112",
        "category": "Immediate Police / Medical / Fire",
        "description": "Pan-India single number for immediate police intervention, fire services, and ambulance emergencies. Accessible without mobile network balance or SIM lock.",
        "description_tamil": "இந்தியா முழுவதும் காவல்துறை, தீயணைப்பு மற்றும் ஆம்புலன்ஸ் அவசர தேவைகளுக்கான ஒருங்கிணைந்த எண். ரீசார்ஜ் இல்லாத போதிலும் இயங்கும்.",
        "available_24_7": True
    },
    {
        "id": "cyber-fraud",
        "name": "National Cyber Crime Helpline",
        "name_tamil": "தேசிய சைபர் கிரைம் உதவி மையம்",
        "number": "1930",
        "category": "Financial Fraud & Cyber Harassment",
        "description": "Critical emergency line to freeze fraudulent banking, UPI, and card debits within the 2-hour Golden Hour window and report online harassment.",
        "description_tamil": "ஆன்லைன் வங்கி மோசடி, UPI பண இழப்பு மற்றும் இணைய அச்சுறுத்தல்களுக்கு உடனடியாக பணம் முடக்க அழைக்க வேண்டிய எண்.",
        "available_24_7": True
    },
    {
        "id": "women-helpline",
        "name": "Women in Distress Helpline",
        "name_tamil": "பெண்கள் உதவி மையம்",
        "number": "181 / 1091",
        "category": "Women Safety & Domestic Abuse",
        "description": "Confidential rescue, legal advice, shelter home coordination, and psychological counseling for women facing violence or distress.",
        "description_tamil": "குடும்ப வன்முறை, பணியிட தொல்லை அல்லது ஆபத்தில் உள்ள பெண்களுக்கு சட்ட ஆலோசனை மற்றும் அடைக்கலம் தரும் மையம்.",
        "available_24_7": True
    },
    {
        "id": "consumer-helpline",
        "name": "National Consumer Helpline (NCH)",
        "name_tamil": "தேசிய நுகர்வோர் உதவி மையம்",
        "number": "1915",
        "category": "Consumer Rights & Fraud Redressal",
        "description": "Toll-free helpline by Ministry of Consumer Affairs for defective goods, non-refunds, e-commerce grievances, and pre-litigation company mediation.",
        "description_tamil": "பொருட்கள் குறைபாடு, உத்தரவாத மறுப்பு மற்றும் ஏமாற்று வர்த்தகத்திற்கு எதிரான அரசு குறைதீர்ப்பு உதவி எண்.",
        "available_24_7": False
    },
    {
        "id": "childline",
        "name": "Childline Emergency Support",
        "name_tamil": "குழந்தைகள் உதவி மையம் (சைல்டுலைன்)",
        "number": "1098",
        "category": "Child Protection & Abuse Rescue",
        "description": "Emergency outreach service for children in need of care, protection from child labour, child marriage, and physical/sexual abuse.",
        "description_tamil": "குழந்தை தொழிலாளர் முறை, குழந்தை திருமணம் மற்றும் பாலியல் வன்முறையிலிருந்து குழந்தைகளை காக்கும் அவசர எண்.",
        "available_24_7": True
    },
    {
        "id": "legal-aid",
        "name": "NALSA National Legal Aid Helpline",
        "name_tamil": "இலவச சட்ட உதவி மையம் (NALSA)",
        "number": "15100",
        "category": "Free Legal Aid & Representation",
        "description": "Statutory helpline under Legal Services Authorities Act for free advocate assignment, bail assistance, and advice for weaker sections and custody detainees.",
        "description_tamil": "வழக்கறிஞர் கட்டணம் செலுத்த இயலாத ஏழை எளிய மக்கள் மற்றும் கைதிகளுக்கு இலவச அரசு சட்ட உதவி தரும் மையம்.",
        "available_24_7": True
    },
    {
        "id": "senior-citizen",
        "name": "Elder Line (Senior Citizens)",
        "name_tamil": "முதியோர் உதவி மையம் (Elder Line)",
        "number": "14567",
        "category": "Senior Citizen Protection & Care",
        "description": "Toll-free national helpline for senior citizens regarding maintenance rights, rescue from abandonment, emotional support, and legal guidance under Maintenance and Welfare of Parents Act.",
        "description_tamil": "முதியோர் பராமரிப்பு, சொத்து பாதுகாப்பு மற்றும் கைவிடப்பட்ட முதியோர்களுக்கான தேசிய உதவி மையம்.",
        "available_24_7": True
    },
    {
        "id": "anti-corruption",
        "name": "Anti-Corruption & Vigilance Helpline",
        "name_tamil": "லஞ்ச ஒழிப்பு மற்றும் ஊழல் தடுப்பு மையம்",
        "number": "1064",
        "category": "Bribe Reporting & Public Vigilance",
        "description": "Direct toll-free line to State Vigilance & Anti-Corruption Bureau to report bribery demands by government servants and schedule trap operations.",
        "description_tamil": "அரசு ஊழியர்கள் லஞ்சம் கேட்டால் உடனடியாக லஞ்ச ஒழிப்புத் துறையிடம் தகவல் தெரிவிக்கும் எண்.",
        "available_24_7": True
    }
]

def get_all_emergency_contacts():
    return EMERGENCY_CONTACTS
