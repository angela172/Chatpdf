import fitz
import re

def clean_text(text):
    text = re.sub(r'[A-Za-z]:\\[^\n]*', '', text)
    text = re.sub(r'Page \d+ of \d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in doc)
    return text

def preprocess_text(text, chunk_size=500):
    words = text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks
def extract_headings(pdf_path):
    """
    Extract headings from a PDF, assuming that headings are styled differently.
    """
    doc = fitz.open(pdf_path)
    headings = []

    # Iterate through each page of the PDF
    for page_number, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    font_size = span["size"]

                    # Check for headings based on font size
                    if font_size > 12 and len(text) > 5:  # Adjust the threshold for what counts as a heading
                        headings.append((text, page_number))
    
    return headings