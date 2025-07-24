# === 📄 utils/llm_audit.py ===
from llama_cpp import Llama

llm = Llama(model_path="llama-3.gguf", n_ctx=2048)

def llm_audit(text):
    prompt = f"""
You are a Policy Audit Expert.
Review the following policy text and return a list of 3 ambiguous or non-compliant clauses in JSON format like:
[{{"issue": "...", "recommendation": "..."}}]

Text:
{text[:3000]}
"""
    response = llm(prompt=prompt, stop=["\n"], max_tokens=512)
    return response["choices"][0]["text"].strip()
