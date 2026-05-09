from openai import OpenAI
import streamlit as st

# ---------------------------------------
# Initialize Client (lazy-safe)
# ---------------------------------------
def get_openai_client_llm():
    api_key = st.secrets.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing in Streamlit secrets.")

    return OpenAI(api_key=api_key)


# ---------------------------------------
# Main LLM Call
# ---------------------------------------
def generate_response_llm(prompt: str, system_prompt: str) -> str:

    try:

        client = get_openai_client_llm()

        return json.dumps({
            "executive_summary": "DEBUG MODE ACTIVE",
            "key_findings": [
                "LLM pipeline reached successfully",
                "Factory operational analysis initialized"
            ],
            "identified_problems": [
                "Testing dashboard rendering"
            ],
            "recommendations": [
                "Verify OpenAI API integration"
            ],
            "risk_level": "Medium",
            "business_outlook": "Debug mode response generated successfully."
        })

    except Exception as e:

        return json.dumps({
            "executive_summary": "ERROR",
            "key_findings": [],
            "identified_problems": [str(e)],
            "recommendations": [],
            "risk_level": "High",
            "business_outlook": "LLM failure."
        })
