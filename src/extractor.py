from google import genai


"""
extractor.py

Purpose:
---------
This file is responsible for:

1. Opening image-based PDFs
2. Converting each page into an image
3. Saving those images locally (for debugging / processing)
4. Returning list of image paths for further AI processing

This file handles the INPUT stage of our pipeline.
"""

import os
import fitz  # PyMuPDF


def convert_pdf_to_images(pdf_path: str, output_folder: str):
    """
    Converts each page of a PDF into a PNG image.

    Parameters:
    -----------
    pdf_path : str
        Path to the input PDF file

    output_folder : str
        Folder where extracted images will be saved

    Returns:
    --------
    list
        List of image file paths created
    """

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    image_paths = []

    # Loop through each page
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]

        # Convert page to image (pixmap)
        pix = page.get_pixmap()

        image_path = os.path.join(
            output_folder, f"page_{page_number + 1}.png"
        )

        # Save image
        pix.save(image_path)

        image_paths.append(image_path)

        print(f"Saved: {image_path}")

    pdf_document.close()

    return image_paths
def list_available_models(api_key: str):
    """
    Prints all models available for this API key.
    """

    client = genai.Client(
        api_key=api_key,
        http_options={"api_version": "v1"}
    )

    models = client.models.list()

    print("\nAVAILABLE MODELS:\n")

    for model in models:
        print(model.name)

def extract_text_from_image(image_path: str, api_key: str):
    """
    Uses Gemini Vision (new SDK) to extract text from an image.
    """

    # Create client
    client = genai.Client(
    api_key=api_key,
    http_options={"api_version": "v1"}
)


    # Read image bytes
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    response = client.models.generate_content(
        model="gemini-2.5-flash",


        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": "Extract all readable text from this inspection or thermal report image. Preserve structure clearly."},
                    {
                        "inline_data": {
                            "mime_type": "image/png",
                            "data": image_bytes
                        }
                    }
                ]
            }
        ]
    )

    return response.text
def extract_text_from_pdf(pdf_path: str):
    """
    Extracts all selectable text directly from a PDF file.

    This avoids converting to images and avoids multiple AI OCR calls.
    """

    pdf_document = fitz.open(pdf_path)

    full_text = ""

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]

        # Extract text from page
        page_text = page.get_text()

        full_text += f"\n\n========== PAGE {page_number + 1} ==========\n\n"
        full_text += page_text

    pdf_document.close()

    print(f"\nFinished extracting text from: {pdf_path}")
    print(f"Total characters extracted: {len(full_text)}\n")

    return full_text
