import fitz  # PyMuPDF

class PDFProcessor:
    def __init__(self):
        pass

    def extract_text(self, pdf_path):
        # Open the PDF with PyMuPDF
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text")  # Extract text from each page
        return text

    def get_summary(self, text, num_sentences=3):
        sentences = text.split('. ')
        return '. '.join(sentences[:num_sentences]) + '.'