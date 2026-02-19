from PyPDF2 import PdfReader

def extract_text_from_pdf(filepath):
    reader = PdfReader(filepath)
    text = []
    for page in reader.pages:
        ptext = page.extract_text() or ""
        text.append(ptext)
    return "\n".join(text)