PROJECT: RESUME-JD SIMILARITY CHECKER

DESCRIPTION
-----------
The application provides a simple interface to upload a resume and a job description file. The backend, built with Django, extracts the text from these documents, parses them to identify relevant sections like skills and responsibilities, and then uses a text vectorization model to compute a similarity score. This score quantifies how well the resume's skills match the job description's requirements. Then one can proceed with chat based interview for now which will take place on the basis of resume and the job description.
---

FEATURES
--------
- File Upload: Easily upload resume and job description files through a user-friendly web interface.
- Text Extraction: Automatically extracts text from uploaded documents.
- Structured Data Parsing: Parses unstructured text from the resume and JD into a structured JSON format, identifying key information like contact details, skills, work experience, and required qualifications.
- Skill Matching: Compares the skills listed in the resume against the required skills in the job description.
- Similarity Score: Calculates and displays a similarity score, providing a quantitative measure of how well the resume matches the job description.
- Interview: AI will act as an interviewer and will take interview of the candidate.
- CORS Support: Includes Cross-Origin Resource Sharing (CORS) headers to allow the frontend to communicate with the backend API from a different origin.

---

UPCOMING FEATURES: VERSION 2.0
------------------------------
The next major version will transform this tool into a comprehensive interview preparation platform by introducing an interactive, AI-powered mock interview feature.

* Real-Time Mock Interviews with LLMs
Once a resume and JD are uploaded and analyzed, users can initiate a real-time practice interview. An AI, powered by a Large Language Model (LLM), will assume the role of an interviewer and conduct a spoken or text-based interview session.

* Dynamic & Contextual Question Generation
The AI interviewer won't ask generic questions. Instead, it will generate questions dynamically based on the content of the uploaded resume and job description. For example:
  - It might ask for more details about a specific project listed on the resume.
  - It could pose a technical challenge related to a required skill in the job description.
  - It may present a behavioral question based on the company's profile and the role's responsibilities.

* Customizable Interview Sessions
Users will have the ability to tailor their practice sessions by selecting:
  - Type of Interview: Choose from different formats like Technical, Behavioral, or a Mixed session.
  - Difficulty Level: Adjust the complexity of the questions (Easy, Medium, or Hard).
  - Number of Rounds: Schedule a single comprehensive interview or simulate a multi-round process by selecting the desired number of rounds.

---

TECHNOLOGIES USED
-----------------
- Backend:
  - Python
  - Django
  - Django REST Framework

- Frontend:
  - HTML
  - CSS
  - JavaScript

- Machine Learning/NLP:
  - Google Embedding Models (e.g., 'text-embedding-004') for text vectorization.
  - NumPy for numerical operations and similarity calculation.

---

SETUP AND INSTALLATION
----------------------
1. Clone the repository:
   git clone <repository-url>

2. Navigate to the project directory:
   cd <project-directory>

3. Install the required dependencies:
   pip install -r requirements.txt

4. Run the Django development server:
   python manage.py runserver
   
   The backend API will be available at http://127.0.0.1:8000.

---

USAGE
-----
1. Open the index.html file in your web browser.
2. Use the form to upload a resume file and a job description file.
3. Click the "Check Similarity" button.
4. The application will display the similarity score, as well as the parsed JSON data from both the job description and the resume.

---

