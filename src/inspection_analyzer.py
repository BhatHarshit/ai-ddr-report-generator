"""
inspection_analyzer.py

Purpose:
---------
Takes full inspection report text
and extracts structured inspection findings.
"""

from google import genai


def analyze_inspection_text(inspection_text: str, api_key: str):

    client = genai.Client(
        api_key=api_key,
        http_options={"api_version": "v1"}
    )

    prompt = f"""
You are a property inspection AI assistant.

Below is the full inspection report text.

Your task:
1. Identify all reported issues.
2. Extract:
   - Area/Room
   - Issue description
   - Severity (if mentioned)
   - Recommended action
3. Summarize overall property condition.
4. Highlight urgent risks.

Return structured output.

INSPECTION REPORT TEXT:
{inspection_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
