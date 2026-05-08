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

            "Summarize Notes": {
                "system_prompt": (
                    "You are a senior business analyst. Provide structured, "
                    "clear, and professional summaries."
                ),
                "prompt": """
Summarize the following business notes.

Return your response in this format:

- Key Points
- Trends
- Risks
- Opportunities

Be concise but insightful.

Business Notes:
{input}
"""
            },

            "Generate Report": {
                "system_prompt": (
                    "You are a professional business consultant creating structured executive reports."
                ),

                "prompt": """
            Analyze the provided business data.

            Return ONLY valid JSON.

            Do not include markdown.
            Do not include explanations.
            Do not wrap the JSON in triple backticks.

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

            "Extract Action Items": {
                "system_prompt": (
                    "You are an operations manager extracting actionable tasks."
                ),
                "prompt": """
From the following business notes, extract clear and actionable tasks.

Return as a bullet list with:
- Task
- Priority (High/Medium/Low)

Data:
{input}
"""
            },

            "Ask Questions": {
                "system_prompt": (
                    "You are a business analyst answering questions based on provided input."
                ),
                "prompt": """
Answer questions based on the provided input.

If the input does not contain enough information, say:
"Not enough information."

Input:
{input}
"""
            }

        }  # end modes

    }  # end AI Dashboard Assistant

}  # end APP_CONFIG
