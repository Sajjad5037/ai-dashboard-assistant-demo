APP_CONFIG = {
    "AI Dashboard Assistant": {

        "title": "📊 AI Dashboard Assistant",

        "description": (
            "Analyze business notes, generate reports, extract action items, "
            "and answer questions based on internal data."
        ),

        "use_case": "Internal business analysis and reporting automation",

        # -------------------------------
        # Input Placeholder
        # -------------------------------
        "input_placeholder": (
            "Paste meeting notes, operational updates, KPIs, or business logs here..."
        ),

        # -------------------------------
        # Example Input
        # -------------------------------
        "example_input": """Q2 revenue dropped by 12% compared to Q1.
Customer churn increased significantly in the last 2 months.
Marketing spend was reduced by 20%.
Customer support tickets increased by 18%.
Product team delayed 2 key feature releases.
Sales team reported lower conversion rates.
""",

        # -------------------------------
        # Modes
        # -------------------------------
        "modes": {

            # =========================================================
            # SUMMARIZE NOTES
            # =========================================================
            "Summarize Notes": {

                "system_prompt": (
                    "You are a structured business analysis API. "
                    "You must always return valid JSON only. "
                    "Never return markdown, explanations, headings, "
                    "or prose outside JSON."
                ),

                "prompt": """
Analyze the provided business notes.

Return ONLY valid JSON.

IMPORTANT:
- Do not include markdown
- Do not include headings
- Do not include explanations
- Do not include triple backticks
- Output must start with {
- Output must end with }

Use this exact schema:

{
  "key_points": [
    "...",
    "..."
  ],
  "trends": [
    "...",
    "..."
  ],
  "risks": [
    "...",
    "..."
  ],
  "opportunities": [
    "...",
    "..."
  ],
  "overall_summary": "..."
}

Business Notes:
{input}
"""
            },

            # =========================================================
            # GENERATE REPORT
            # =========================================================
            "Generate Report": {

                "system_prompt": (
                    "You are a structured business analysis API. "
                    "You must always return valid JSON only. "
                    "Never return markdown, explanations, headings, "
                    "or prose outside JSON."
                ),

                "prompt": """
Analyze the provided business data.

Return ONLY valid JSON.

IMPORTANT:
- Do not include markdown
- Do not include headings
- Do not include explanations
- Do not include triple backticks
- Output must start with {
- Output must end with }

Use this exact schema:

{
  "executive_summary": "...",
  "key_findings": [
    "...",
    "..."
  ],
  "identified_problems": [
    "...",
    "..."
  ],
  "recommendations": [
    "...",
    "..."
  ],
  "risk_level": "Low/Medium/High",
  "business_outlook": "..."
}

Business Data:
{input}
"""
            },

            # =========================================================
            # EXTRACT ACTION ITEMS
            # =========================================================
            "Extract Action Items": {

                "system_prompt": (
                    "You are a structured operations workflow API. "
                    "You must always return valid JSON only."
                ),

                "prompt": """
Extract actionable operational tasks from the provided business notes.

Return ONLY valid JSON.

IMPORTANT:
- Do not include markdown
- Do not include headings
- Do not include explanations
- Do not include triple backticks
- Output must start with {
- Output must end with }

Use this exact schema:

{
  "action_items": [
    {
      "task": "...",
      "priority": "High/Medium/Low",
      "owner_recommendation": "...",
      "deadline_urgency": "Immediate/Soon/Normal"
    }
  ],
  "overall_priority": "Low/Medium/High"
}

Business Notes:
{input}
"""
            },

            # =========================================================
            # ASK QUESTIONS
            # =========================================================
            "Ask Questions": {

                "system_prompt": (
                    "You are a structured business Q&A API. "
                    "You must always return valid JSON only."
                ),

                "prompt": """
Answer the business question based on the provided input.

Return ONLY valid JSON.

IMPORTANT:
- Do not include markdown
- Do not include headings
- Do not include explanations
- Do not include triple backticks
- Output must start with {
- Output must end with }

If there is insufficient information,
clearly state that in the response.

Use this exact schema:

{
  "question_answered": true,
  "answer": "...",
  "confidence_level": "Low/Medium/High",
  "supporting_points": [
    "...",
    "..."
  ]
}

Business Input:
{input}
"""
            }

        }  # end modes

    }  # end AI Dashboard Assistant

}  # end APP_CONFIG
