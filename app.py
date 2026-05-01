import streamlit as st
from config import APP_CONFIG
from prompt_engine import build_prompt
from llm import generate_response_llm

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Demo Suite",
    layout="wide"
)

# -------------------------------
# Select App (Foundation Switch)
# -------------------------------
app_name = st.sidebar.selectbox(
    "Select Demo",
    list(APP_CONFIG.keys())
)

config = APP_CONFIG[app_name]

# -------------------------------
# Header
# -------------------------------
st.title(config["title"])
st.info(config["use_case"])
st.write(config["description"])

# -------------------------------
# Mode Selector
# -------------------------------
mode = st.sidebar.selectbox(
    "Select Task",
    list(config["modes"].keys())
)

mode_config = config["modes"][mode]

# -------------------------------
# Session State Init
# -------------------------------
if "input_text_main" not in st.session_state:
    st.session_state.input_text_main = ""

if "output_text_main" not in st.session_state:
    st.session_state.output_text_main = ""

# -------------------------------
# Input Section
# -------------------------------
col_input, col_actions = st.columns([4, 1])

with col_input:
    user_input = st.text_area(
        "Enter your data:",
        value=st.session_state.input_text_main,
        height=260,
        placeholder=config.get("input_placeholder", "")
    )

with col_actions:
    st.write("")
    st.write("")

    if st.button("Load Example"):
        st.session_state.input_text_main = config["example_input"]
        st.rerun()

    if st.button("Clear"):
        st.session_state.input_text_main = ""
        st.session_state.output_text_main = ""
        st.rerun()
# -------------------------------
# Generate Button
# -------------------------------
generate_clicked = st.button("Generate", use_container_width=True)

# -------------------------------
# Processing
# -------------------------------
if generate_clicked:
    if not user_input.strip():
        st.warning("Please enter some input before generating.")
    else:
        template = mode_config["prompt"]
        

        prompt = build_prompt(template, user_input)

        with st.spinner("Analyzing..."):
            try:
                system_prompt = mode_config["system_prompt"]
                output = generate_response_llm(prompt, system_prompt)
                st.session_state.output_text_main = output
            except Exception as e:
                st.error(f"Error: {str(e)}")

# -------------------------------
# Output Section
# -------------------------------
if st.session_state.output_text_main:
    st.divider()
    st.subheader(f"{mode} Output")

    st.success("Analysis complete")

    st.markdown(st.session_state.output_text_main)
# -------------------------------
# Footer (Subtle Branding)
# -------------------------------
st.divider()
st.caption("Demo: AI-powered workflow automation | Built with Streamlit + OpenAI")
