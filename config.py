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
        # Example Input (VERY IMPORTANT)
        # -------------------------------
        "example_input": """Q2 revenue dropped by 12% compared to Q1.
Customer churn increased significantly in the last 2 months.
Marketing spend was reduced by 20%.
Customer support tickets increased by 18%.
Product team delayed 2 key feature releases.
Sales team reported lower conversion rates.
""",

        # -------------------------------
        # Modes (Core Functionality)
        # -------------------------------
        "modes": {

            # ---------------------------
            # Summarization Mode
            # ---------------------------
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

            # ---------------------------
            # Report Generation
            # ---------------------------
            "Generate Report": {
                "system_prompt": (
                    "You are a professional business consultant writing reports for executives."
                ),

                "prompt": """
Create a structured business report based on the following data.

Include:

1. Executive Summary
2. Key Findings
3. Problems Identified
4. Recommendations

Keep it professional and decision-focused.

Data:
{input}
"""
            },

            # ---------------------------
            # Action Extraction
            # ---------------------------
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

            # ---------------------------
            # Q&A Mode
            # ---------------------------
            "Ask Questions": {
                "system_prompt": (
                    "You are a business analyst answering questions based on provided context."
                ),

                "prompt": """
You are a business analyst.

Context:
{context}

User Question:
{input}

Rules:
- If context is provided, base your answer on it
- If no context is provided, use general business knowledge
- Be clear, practical, and concise

Answer:
"""
            }
        }
    }
}
