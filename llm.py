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
    """
    Generates response using OpenAI Chat API.

    Args:
        prompt (str): user prompt
        system_prompt (str): system role instruction

    Returns:
        str: model response
    """

    client = get_openai_client_llm()

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        # Clean error for UI
        return f"Error generating response: {str(e)}"
