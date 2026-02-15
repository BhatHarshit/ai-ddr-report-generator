"""
thermal_analyzer.py

Purpose:
---------
Takes full extracted thermal document text
and converts it into structured findings.
"""

from google import genai


def analyze_thermal_text(thermal_text: str, api_key: str):

    client = genai.Client(
        api_key=api_key,
        http_options={"api_version": "v1"}
    )

    prompt = f"""
You are a building inspection AI assistant.

Below is the full extracted text from a thermal inspection document.

Your task:
1. Identify all thermal images/pages.
2. Extract:
   - Date
   - Location/Area (if available)
   - Hotspot temperature
   - Coldspot temperature
   - Emissivity
   - Reflected temperature
3. Summarize thermal anomalies.
4. Identify possible causes.
5. Rate severity (Low / Moderate / High).

Return the result in clean structured format.

THERMAL DOCUMENT TEXT:
{thermal_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
