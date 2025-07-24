# === 📄 utils/rules.py ===
REQUIRED_FIELDS = ["Policy Number", "Effective Date", "Holder Name", "Coverage", "Terms"]

def static_checks(text):
    issues = []
    for field in REQUIRED_FIELDS:
        if field.lower() not in text.lower():
            issues.append({"type": "missing", "field": field})
    return issues
