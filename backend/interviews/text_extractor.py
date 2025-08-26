import os
import docx
import PyPDF2

class TextExtractor:
    def __init__(self, file):
        self.file_name = file.name
        self.file = file

    def extract_text(self):
        ext = os.path.splitext(self.file_name)[-1].lower()
        if ext == '.txt':
            return self._extract_from_txt()
        elif ext == '.docx':
            return self._extract_from_docx()
        elif ext == '.pdf':
            return self._extract_from_pdf()
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        
    def _extract_from_txt(self):
        self.file.seek(0)
        text = self.file.read().decode('utf-8')
        if not text.strip():
            raise ValueError("The text file is empty.")
        return text.strip()
        
    def _extract_from_docx(self):
        self.file.seek(0)
        doc = docx.Document(self.file)
        text = '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
        if not text:
            raise ValueError("The document is empty or contains no text.")
        return text
    
    def _extract_from_pdf(self):
        text = []
        self.file.seek(0)
        reader = PyPDF2.PdfReader(self.file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text.strip())
        if not text:
            raise ValueError("The PDF is empty or contains no text.")
        return '\n'.join(text)