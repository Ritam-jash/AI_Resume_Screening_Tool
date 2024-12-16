from app.utils.pdf_parser import extract_text_from_pdf

# Define paths for various test PDF files
valid_pdf_path = 'sample_resume.pdf'               # Standard text resume
image_pdf_path = 'resume_with_image.pdf'           # Resume with images and text
table_pdf_path = 'resume_with_table.pdf'           # Resume with table/column layout
non_pdf_path = 'sample_resume.txt'                 # Non-PDF file
corrupted_pdf_path = 'corrupted_sample.pdf'        # Corrupted or empty PDF file
non_existent_path = 'non_existent_file.pdf'        # Non-existent file

def test_pdf_parsing():
    # Testing valid PDF file
    print("Testing valid PDF file:")
    try:
        text = extract_text_from_pdf(valid_pdf_path)
        print(text)  # Print extracted text for verification
    except Exception as e:
        print(f"Error: {e}")

    # Testing PDF with images and text
    print("\nTesting PDF with images:")
    try:
        text = extract_text_from_pdf(image_pdf_path)
        print(text)  # Ensure it extracts text without errors
    except Exception as e:
        print(f"Error: {e}")

    # Testing PDF with tables or columns
    print("\nTesting PDF with tables/columns:")
    try:
        text = extract_text_from_pdf(table_pdf_path)
        print(text)  # Ensure it extracts text from tables/columns correctly
    except Exception as e:
        print(f"Error: {e}")

    # Testing non-PDF file
    print("\nTesting non-PDF file:")
    try:
        text = extract_text_from_pdf(non_pdf_path)
        print(text)
    except Exception as e:
        print(f"Error: {e}")

    # Testing corrupted or empty PDF file
    print("\nTesting corrupted/empty PDF file:")
    try:
        text = extract_text_from_pdf(corrupted_pdf_path)
        print(text)
    except Exception as e:
        print(f"Error: {e}")

    # Testing non-existent file path
    print("\nTesting non-existent file path:")
    try:
        text = extract_text_from_pdf(non_existent_path)
        print(text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_pdf_parsing()
