# ---------------------------------------
# Core Prompt Builder
# ---------------------------------------
def build_prompt(template: str, user_input: str) -> str:
    """
    Injects user input into a prompt template.

    Args:
        template (str): prompt template containing {input}
        user_input (str): user-provided text

    Returns:
        str: final prompt
    """

    if not template:
        raise ValueError("Prompt template is empty.")

    if not user_input:
        raise ValueError("User input is empty.")

    return template.replace("{input}", user_input.strip())


# ---------------------------------------
# Optional: Context-Aware Prompt Builder
# (use later for chat / memory features)
# ---------------------------------------
def build_prompt_with_context(prompt_template: str, user_input: str, context: str = "") -> str:
    """
    Builds prompt with optional additional context.

    Args:
        prompt_template (str): template containing {input} and optionally {context}
        user_input (str): user input
        context (str): extra context (history, docs, etc.)

    Returns:
        str: final prompt
    """

    prompt = prompt_template.replace("{input}", user_input.strip())

    if "{context}" in prompt_template:
        prompt = prompt.replace("{context}", context.strip())

    return prompt


# ---------------------------------------
# Optional: Structured Guard (future use)
# ---------------------------------------
def validate_prompt_variables(prompt_template: str):
    """
    Ensures required placeholders exist.

    Raises:
        ValueError if {input} is missing
    """

    if "{input}" not in prompt_template:
        raise ValueError("Prompt template must include '{input}' placeholder.")
