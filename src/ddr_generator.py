"""
ddr_generator.py

Purpose:
---------
Combines structured thermal and inspection findings
into a final DDR report.
"""

from google import genai


def generate_ddr_report(thermal_summary: str, inspection_summary: str, api_key: str):

    client = genai.Client(
        api_key=api_key,
        http_options={"api_version": "v1"}
    )

    prompt = f"""
You are a professional building diagnostics AI.

Using the structured thermal findings and structured inspection findings below,
generate a complete Diagnostic Defect Report (DDR).

Structure the final report as:

1. Executive Summary
2. Property Condition Overview
3. Thermal Findings Summary
4. Inspection Findings Summary
5. Correlated Issues (where thermal + inspection relate)
6. Severity Assessment (Low / Moderate / High per issue)
7. Root Cause Analysis
8. Recommended Corrective Actions
9. Urgent Risks
10. Missing or Unclear Information

THERMAL STRUCTURED DATA:
{thermal_summary}

INSPECTION STRUCTURED DATA:
{inspection_summary}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
