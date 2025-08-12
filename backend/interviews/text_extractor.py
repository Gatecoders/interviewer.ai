import os
import docx
import PyPDF2

class TextExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        ext = os.path.splitext(self.file_path)[-1].lower()
        if ext == '.txt':
            return self._extract_from_txt()
        elif ext == '.docx':
            return self._extract_from_docx()
        elif ext == '.pdf':
            return self._extract_from_pdf()
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        
    def _extract_from_txt(self):
        with open(self.file_path, 'r', encoding = 'utf-8') as file:
            text = file.read(file)
        if not text.strip():
            raise ValueError("The text file is empty.")
        return text.strip()
        
    def _extract_from_docx(self):
        doc = docx.Document(self.file_path)
        text = '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
        if not text:
            raise ValueError("The document is empty or contains no text.")
        return text
    
    def _extract_from_pdf(self):
        text = []
        with open(self.file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text.strip())
            if not text:
                raise ValueError("The PDF is empty or contains no text.")
        return '\n'.join(text)
