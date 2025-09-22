> **IMPORTANT: USAGE RESTRICTIONS** ⚠️
>
> This is a portfolio project. The source code is public for demonstration purposes only. You are welcome to view and fork the repository to inspect the code, but you are **not permitted** to use, copy, modify, or distribute any part of this code in your own projects. All rights are reserved.

Resume-JD Similarity & Interview Prep Platform

Bridge the gap between your resume and your dream job by analyzing resume-job description fit and practicing with a dynamic AI interviewer.



This tool provides a quantitative similarity score between a resume and a job description and allows candidates to practice for interviews with an AI that asks questions based on their specific resume and the target job.

---

FEATURES
--------
* Seamless Document Upload: Easily upload your resume and the job description in various formats (e.g., PDF, DOCX).
* Intelligent Text Parsing: Automatically extracts and structures key information from unstructured text, identifying contact details, skills, work experience, and required qualifications into JSON format.
* Similarity Scoring: Leverages Google's text embedding models to calculate a precise similarity score, giving you a clear measure of your resume's alignment with the job requirements.
* AI-Powered Chat Interview: Engage in a preliminary text-based interview with an AI that uses the context of your resume and the job description to ask relevant questions.

---

UPCOMING IN VERSION 2.0: THE INTERVIEW COACH
------------------------------------------------------
The next major version will transform this tool into a comprehensive interview preparation platform.

* Real-Time Mock Interviews: Practice a full interview with an LLM-powered AI that acts as the interviewer in a spoken or text-based session.
* Dynamic & Contextual Questions: The AI generates questions tailored specifically to your resume and the job description. For example:
    * "Tell me more about your role in the 'Project X' you listed on your resume."
    * "This role requires extensive experience with Kubernetes. Can you describe a complex deployment you've managed?"
* Customizable Interview Sessions: Tailor your practice by selecting the interview type (Technical, Behavioral), difficulty level, and number of rounds.

---

TECH STACK
----------
* Backend:
    * Python
    * Django
    * Django REST Framework
* Frontend:
    * HTML
    * CSS
    * JavaScript
* AI / NLP:
    * Google Embedding Models (e.g., text-embedding-004)
    * NumPy

---

SETUP AND INSTALLATION
----------------------

Prerequisites
* Python 3.8+
* pip (Python package installer)

Installation Steps

1.  Clone the repository:
    git clone <repository-url>
    cd <project-directory>

2.  Create and activate a virtual environment:
    * Windows:
        python -m venv venv
        .\venv\Scripts\activate
    * macOS / Linux:
        python3 -m venv venv
        source venv/bin/activate

3.  Install the required dependencies:
    pip install -r requirements.txt

4.  Set up environment variables:
    Create a file named .env in the root project directory and add your Google API Key.
    
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"

    You can obtain a free Google API key from the Google AI for Developers website (https://ai.google.dev/).

5.  Apply database migrations:
    python manage.py migrate

6.  Run the development server:
    python manage.py runserver

    The backend API will be available at http://127.0.0.1:8000.

---

USAGE
-----
1.  Open the index.html file in your web browser.
2.  Upload your resume file and a job description file using the form.
3.  Click the "Check Similarity" button.
4.  The application will display the similarity score and the parsed JSON data from both documents.
5.  You can then proceed to the chat interface to begin your interview session.
