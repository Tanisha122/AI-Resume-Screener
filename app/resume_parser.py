from pdfminer.high_level import extract_text
from docx import Document
import os

def parse_resume(file_path):
    """
    Parse a resume file (PDF or DOCX) and return plain text.

    Args:
        file_path (str): Path to the resume file.

    Returns:
        str: Extracted plain text from the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.pdf':
        # Parse PDF file
        try:
            text = extract_text(file_path)
        except Exception as e:
            raise ValueError(f"Error parsing PDF file: {e}")
    elif file_extension == '.docx':
        # Parse DOCX file
        try:
            doc = Document(file_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        except Exception as e:
            raise ValueError(f"Error parsing DOCX file: {e}")
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")

    return text