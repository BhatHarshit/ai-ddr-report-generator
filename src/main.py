"""
main.py

FULL AI DDR PIPELINE

Stage 1:
- Extract full text from Thermal PDF
- Extract full text from Inspection PDF

Stage 2:
- Send ONE Gemini request for Thermal structuring
- Send ONE Gemini request for Inspection structuring

Stage 3:
- Send ONE Gemini request to generate Final DDR Report

Outputs:
- Raw extracted text files
- Structured AI summaries
- Final DDR Report
"""

import os
from dotenv import load_dotenv

from extractor import extract_text_from_pdf
from thermal_analyzer import analyze_thermal_text
from inspection_analyzer import analyze_inspection_text
from ddr_generator import generate_ddr_report


def main():

    print("\n========== AI DDR REPORT PIPELINE ==========\n")

    # ----------------------------------
    # Load API Key
    # ----------------------------------

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    # ----------------------------------
    # File Paths
    # ----------------------------------

    thermal_pdf = os.path.join("data", "Thermal Images.pdf")
    inspection_pdf = os.path.join("data", "Sample Report.pdf")

    os.makedirs("output", exist_ok=True)

    # ----------------------------------
    # Stage 1: Text Extraction (LOCAL)
    # ----------------------------------

    print("Stage 1: Extracting Thermal PDF text...")
    thermal_text = extract_text_from_pdf(thermal_pdf)

    print("Stage 1: Extracting Inspection PDF text...")
    inspection_text = extract_text_from_pdf(inspection_pdf)

    # Save raw extracted text
    with open(os.path.join("output", "thermal_raw.txt"), "w", encoding="utf-8") as f:
        f.write(thermal_text)

    with open(os.path.join("output", "inspection_raw.txt"), "w", encoding="utf-8") as f:
        f.write(inspection_text)

    print("\nRaw extraction complete.")
    print(f"Thermal Text Characters: {len(thermal_text)}")
    print(f"Inspection Text Characters: {len(inspection_text)}")

    # ----------------------------------
    # Stage 2: AI Structuring (2 Calls)
    # ----------------------------------

    print("\nStage 2: Analyzing Thermal Document with Gemini...")
    thermal_summary = analyze_thermal_text(thermal_text, api_key)

    print("Stage 2: Analyzing Inspection Document with Gemini...")
    inspection_summary = analyze_inspection_text(inspection_text, api_key)

    # Save structured outputs
    with open(os.path.join("output", "thermal_structured.txt"), "w", encoding="utf-8") as f:
        f.write(thermal_summary)

    with open(os.path.join("output", "inspection_structured.txt"), "w", encoding="utf-8") as f:
        f.write(inspection_summary)

    print("Structured AI summaries saved.")

    # ----------------------------------
    # Stage 3: Final DDR Report (1 Call)
    # ----------------------------------

    print("\nStage 3: Generating Final DDR Report...")
    final_ddr = generate_ddr_report(
        thermal_summary,
        inspection_summary,
        api_key
    )

    with open(os.path.join("output", "final_ddr_report.txt"), "w", encoding="utf-8") as f:
        f.write(final_ddr)

    print("Final DDR report saved.")

    # ----------------------------------

    print("\n========== FULL AI DDR PIPELINE COMPLETE ==========\n")


if __name__ == "__main__":
    main()
