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

    client = get_openai_client_llm()

    try:

        print("✅ OpenAI client initialized")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            response_format={"type": "json_object"}
        )

        print("✅ OpenAI response received")

        content = response.choices[0].message.content

        print("✅ Response content extracted")

        if not content:
            raise ValueError("Empty response received from model.")

        print("✅ Returning response")

        return content.strip()

    except Exception as e:

        print("❌ OpenAI API Exception:")
        print(str(e))

        raise e
