import PyPDF2
import pytesseract
from pdf2image import convert_from_path
import os


def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                    print(f"[Warning: Unable to extract text from page {page_num + 1}]")
        
        # If no text was extracted, try OCR as a fallback
        if not text.strip():
            print("No text extracted. Attempting OCR...")
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                ocr_text = pytesseract.image_to_string(image)
                print(f"[OCR Page {i + 1}]: {ocr_text[:100]}")  # Log first 100 characters
                text += ocr_text
        
        if not text.strip():
            print("Error: No text could be extracted from the PDF.")
            return ""
        
        print(f"Extracted Resume Text: {text[:500]}")  # Log first 500 characters
        return text

    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
        return ""
