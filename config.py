APP_CONFIG = {
    "AI Factory Operations Intelligence": {

        "title": "🏭 AI Factory Operations Intelligence",

        "description": (
            "Analyze factory operational updates, generate executive intelligence "
            "reports, identify production risks, and improve operational visibility "
            "across manufacturing workflows."
        ),

        "use_case": (
            "AI-assisted factory operations intelligence and production monitoring"
        ),

        "input_placeholder": (
            "Submit machine issues, production delays, QC findings, dispatch risks, "
            "inventory shortages, or operational updates..."
        ),

        "example_input": """
Machine #12 experienced repeated thread breakage during large logo embroidery runs for export hoodies.

Production throughput dropped significantly during the evening shift, and operators reported increasing delays in order completion.

Three urgent export orders scheduled for tomorrow’s dispatch may not be completed on time if downtime continues.

QC teams also reported increased stitching inconsistencies on premium garments requiring additional rework.
""",

        "mode": {

            "system_prompt": (
                "You are an AI factory operations intelligence system. "
                "Your role is to convert raw factory operational reports into "
                "structured executive intelligence for factory owners and managers. "
                "You analyze production workflows, machine downtime, dispatch risk, "
                "quality control issues, inventory constraints, and operational impact. "
                "You must always return valid JSON only. "
                "Never return markdown, explanations, headings, "
                "or prose outside JSON."
            ),

            "prompt": """
Analyze the provided factory operational report.

Identify:
- production bottlenecks
- machine performance issues
- dispatch risks
- operational impact
- quality control concerns
- management priorities
- business consequences

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

Factory Operational Report:
{input}
"""
        }
    }
}
