AI-Powered Diagnostic Defect Report (DDR) Generator
Project Overview

This project is an AI-powered pipeline that automatically generates a Diagnostic Defect Report (DDR) from property inspection documents.

It accepts:

A Thermal Inspection PDF

A General Property Inspection PDF

The system extracts the contents of both documents, analyzes them using AI, correlates findings, and produces a structured, professional DDR report.

Problem It Solves

Manually reviewing inspection reports and thermal scans is time-consuming and requires cross-referencing multiple documents.

This system automates:

Extraction of inspection findings

Thermal anomaly detection

Correlation between thermal and visual observations

Structured report generation

The result is a consistent, structured, and AI-assisted diagnostic report.

Why AI Is Used

AI is used to:

Interpret semi-structured inspection text

Identify anomalies and severity levels

Perform cross-document reasoning

Generate a coherent final diagnostic report

Traditional rule-based parsing would not handle layout variation and contextual reasoning effectively.

System Architecture
Input PDFs
   ↓
Text Extraction (PyMuPDF - Local Processing)
   ↓
Thermal AI Structuring (Gemini API Call 1)
Inspection AI Structuring (Gemini API Call 2)
   ↓
Final DDR Synthesis (Gemini API Call 3)
   ↓
Diagnostic Defect Report (Text Output)


The pipeline is optimized to use only 3 API calls total, ensuring efficiency and compliance with API rate limits.

ETL Pipeline Explanation

This system follows a clear ETL (Extract, Transform, Load) architecture.

Stage 1 — Extract

Handled by: extractor.py

Extracts all selectable text from PDFs using PyMuPDF

No OCR required

No AI calls used at this stage

Outputs raw text files for debugging and traceability

Stage 2 — Transform

Handled by:

thermal_analyzer.py

inspection_analyzer.py

Each document is processed independently using one Gemini API call.

This stage:

Structures findings

Extracts temperatures, severity, and issues

Identifies anomalies

Produces structured summaries

Stage 3 — Load

Handled by: ddr_generator.py

This stage:

Combines both structured summaries

Performs cross-document reasoning

Generates the final Diagnostic Defect Report

Initial Approach & Optimization

Initially, the system attempted image-based OCR using Gemini Vision on each PDF page.

However, this approach:

Required one API call per page

Risked hitting API rate limits

Increased latency and cost

The architecture was refactored to:

Extract text locally using PyMuPDF

Reduce API usage to only three calls

Improve performance and reliability

This optimization significantly improved system efficiency.

Project Structure
ai-ddr-report-builder/
│
├── data/                  # Input PDFs
│   ├── Thermal Images.pdf
│   └── Sample Report.pdf
│
├── src/                   # Core pipeline logic
│   ├── main.py
│   ├── extractor.py
│   ├── thermal_analyzer.py
│   ├── inspection_analyzer.py
│   └── ddr_generator.py
│
├── output/                # Generated outputs (ignored in Git)
├── requirements.txt
├── .env                   # Contains API key (not committed)
└── README.md

How to Run

Clone the repository

git clone <your-repo-url>
cd ai-ddr-report-builder


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Create a .env file and add:

GEMINI_API_KEY=your_api_key_here


Run the pipeline

python src/main.py


The final report will be generated in the output/ folder.

Technologies Used

Python

PyMuPDF (PDF text extraction)

Google Gemini API

python-dotenv

Future Improvements

Export final report as DOCX or PDF

Add structured JSON output option

Add support for scanned (image-only) PDFs via OCR fallback

Build a web interface for upload and report download

Add logging and monitoring layer
