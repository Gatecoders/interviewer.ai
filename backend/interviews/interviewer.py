import google.generativeai as genai # <-- FIX 1: Corrected import
import json
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
my_api_key = os.getenv("GOOGLE_API_KEY")
if not my_api_key:
    raise ValueError("API key not found. Please check your .env file and its location.")
genai.configure(api_key=my_api_key)

class AIAssistedInterviewer:
    def __init__(self, jd_data=None, resume_data=None, interview_type="Technical", \
                 difficulty_level="Medium", history=None):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        if history:
            self.chat = self.model.start_chat(history=history)
        elif jd_data or resume_data:
            master_prompt = self._create_master_prompt(
                jd_data, resume_data, interview_type, difficulty_level
            )
            self.chat = self.model.start_chat(history=[
                {'role': 'user', 'parts': [master_prompt]},
                {'role': 'model', 'parts': ["Understood. I will now act as an expert interviewer. I am ready to begin."]}
            ])
        else:
            raise ValueError("Must provide either history or both jd_data and resume_data.")
        
    def _create_master_prompt(self, jd_data, resume_data, interview_type, difficulty_level):
        jd_string = json.dumps(jd_data, indent=2)
        resume_string = json.dumps(resume_data, indent=2)

        prompt = f"""
        You are an expert {'technical' if interview_type == 'Technical' else ''} interviewer at {jd_data.get('company', 'the company')}.
        Your goal is to conduct a professional interview for the '{jd_data.get('role', 'advertised')}' role.

        **CONTEXT:**
        Job Description: {jd_string}
        Candidate's Resume: {resume_string}

        **INSTRUCTIONS:**
        - Interview difficulty: '{difficulty_level}'.
        - Ask questions one at a time.
        - Base your questions on the resume and JD.
        - Ask relevant follow-up questions.
        - Do not reveal you are an AI.
        
        Start the interview now by introducing yourself and asking the candidate for their introduction.
        """
        return prompt

    def start_interview(self):
        try:
            response = self.chat.send_message("Let's begin.")
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"

    def process_candidate_response(self, candidate_answer: str):
        if not candidate_answer:
            return "Please provide a response."
        try:
            response = self.chat.send_message(candidate_answer)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"


# if __name__ == '__main__':
#     # Assume jd_data and resume_data are the JSON objects you parsed earlier
#     jd_data = {'role': 'Data Analyst', 'company': 'Innovatech Solutions', 'required_skills': ['SQL', 'Python', 'Tableau']}
#     resume_data = {'name': 'Priya Sharma', 'skills': {'Data Analysis': ['SQL', 'Python', 'Tableau']}, 'projects': [{'project_name': 'E-commerce Sales Analysis'}]}
    
#     # 1. Initialize the interviewer
#     interviewer = AIAssistedInterviewer(jd_data, resume_data, difficulty_level="Hard")
    
#     # 2. Get the first question
#     ai_question = interviewer.start_interview()
#     print(f"Interviewer: {ai_question}")

#     # 3. Simulate the conversation
#     candidate_answer_1 = "My name is Priya Sharma. I am a data analyst with over 4 years of experience, specializing in SQL and Python to drive business insights."
#     print(f"\nCandidate: {candidate_answer_1}")
    
#     ai_question_2 = interviewer.process_candidate_response(candidate_answer_1)
#     print(f"\nInterviewer: {ai_question_2}")

#     candidate_answer_2 = "In my 'E-commerce Sales Analysis' project, I used Python with Pandas to clean the data and SQL to query sales patterns. I then built a Tableau dashboard to visualize the results, which helped identify our top-performing product categories."
#     print(f"\nCandidate: {candidate_answer_2}")
    
#     ai_question_3 = interviewer.process_candidate_response(candidate_answer_2)
#     print(f"\nInterviewer: {ai_question_3}")