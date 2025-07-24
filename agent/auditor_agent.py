# === 📄 agent/auditor_agent.py ===
from utils.rules import static_checks
from utils.llm_audit import llm_audit
import json

def audit_policy(text):
    static_issues = static_checks(text)

    try:
        raw = llm_audit(text)
        llm_issues = json.loads(raw)
    except Exception as e:
        llm_issues = [{"issue": "LLM audit failed", "recommendation": str(e)}]

    return {
        "summary": {
            "missing_fields": len(static_issues),
            "llm_flags": len(llm_issues)
        },
        "static_check": static_issues,
        "llm_audit": llm_issues
    }
