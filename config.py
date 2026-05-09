APP_CONFIG = {
    "AI Dashboard Assistant": {

        "title": "🏭 AI Factory Operations Intelligence",

        "description": (
            "Analyze factory operational updates, generate production intelligence "
            "reports, identify operational risks, and support management "
            "decision-making across production workflows."
        ),

        "use_case": (
            "AI-assisted factory operations intelligence and production reporting"
        ),

        # -------------------------------
        # Input Placeholder
        # -------------------------------
        "input_placeholder": (
            "Submit machine issues, production delays, QC findings, dispatch risks, "
            "inventory shortages, or factory operational updates..."
        ),

        # -------------------------------
        # Example Input
        # -------------------------------
        "example_input": """
Machine #12 experienced repeated thread breakage during large logo embroidery runs for export hoodies.

Production throughput dropped significantly during the evening shift, and operators reported increasing delays in order completion.

Three urgent export orders scheduled for tomorrow’s dispatch may not be completed on time if downtime continues.

QC teams also reported increased stitching inconsistencies on premium garments requiring additional rework.
""",

        # -------------------------------
        # Modes
        # -------------------------------
        "modes": {

            # =========================================================
            # ANALYZE FACTORY REPORTS
            # =========================================================
            "Analyze Factory Reports": {

                "system_prompt": (
                    "You are an AI factory operations intelligence system. "
                    "Your role is to analyze factory operational reports related to "
                    "production workflows, machine performance, quality control, "
                    "dispatch operations, inventory issues, and operational bottlenecks. "
                    "You must always return valid JSON only. "
                    "Never return markdown, explanations, headings, "
                    "or prose outside JSON."
                ),

                "prompt": """
Analyze the provided factory operational report.

Identify:
- production risks
- machine-related issues
- dispatch risks
- quality control concerns
- operational bottlenecks
- workflow disruptions
- operational trends

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
  "operational_trends": [
    "...",
    "..."
  ],
  "identified_risks": [
    "...",
    "..."
  ],
  "operational_opportunities": [
    "...",
    "..."
  ],
  "overall_operational_summary": "..."
}

Factory Operational Report:
{input}
"""
            },

            # =========================================================
            # GENERATE OPERATIONS INTELLIGENCE
            # =========================================================
            "Generate Operations Intelligence": {

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
  "factory_operations_outlook": "..."
}

Factory Operational Report:
{input}
"""
            },

            # =========================================================
            # EXTRACT OPERATIONAL ACTIONS
            # =========================================================
            "Extract Operational Actions": {

                "system_prompt": (
                    "You are an AI factory workflow coordination system. "
                    "Your role is to extract actionable operational tasks from "
                    "factory production reports and operational updates. "
                    "You must always return valid JSON only."
                ),

                "prompt": """
Extract actionable operational tasks from the provided factory operational report.

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

Factory Operational Report:
{input}
"""
            },

            # =========================================================
            # FACTORY OPERATIONS Q&A
            # =========================================================
            "Factory Operations Q&A": {

                "system_prompt": (
                    "You are an AI factory operations intelligence assistant. "
                    "Your role is to answer operational questions related to "
                    "production workflows, machine performance, dispatch operations, "
                    "quality control, inventory issues, and operational efficiency. "
                    "You must always return valid JSON only."
                ),

                "prompt": """
Answer the factory operations question based on the provided operational report.

Return ONLY valid JSON.

IMPORTANT:
- Do not include markdown
- Do not include headings
- Do not include explanations
- Do not include triple backticks
- Output must start with {
- Output must end with }

If there is insufficient operational information,
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

Factory Operational Input:
{input}
"""
            }

        }

    }

}
