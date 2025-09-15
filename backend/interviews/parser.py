import os
from google import genai
from dotenv import load_dotenv
import logging
import json

logger = logging.getLogger(__name__)

class JdParser:
    def jd_parser(self, text):
        load_dotenv()
        client = genai.Client()
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents = f"""
                    Extract the following details from the job description provided below.
                    Format the output as a valid JSON object. The keys must be exactly as specified here.
                    The values for 'key_responsibilities' and 'required_skills' should be a list of strings.
                    If any piece of information is not found, use a JSON null value.

                    JSON Schema:
                    {{
                    "company_name": "string",
                    "job_title": "string",
                    "key_responsibilities": ["string", "string", ...],
                    "required_skills": ["string", "string", ...]
                    }}

                    Job Description Text:
                    ---
                    {text}
                    ---

                    JSON Output:
                    """
            )
            raw_text = response.text
            if raw_text.startswith("```json"):
                clean_text = raw_text.strip().removeprefix("```json").removesuffix("```")
            else:
                clean_text = raw_text
            parsed_data = json.loads(clean_text)
            return parsed_data

        except Exception as e:
            logger.error(f"Error during JD parsing: {e}")
            return None
        
class ResumeParser:
    def resume_parser(self, text):
        load_dotenv()
        client = genai.Client()
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents = f"""
                    Extract the following professional details from the resume text provided below.
                    Format the output as a valid JSON object. The keys must be exactly as specified in the schema.

                    - The 'skills' key should be an object where each key is a skill category and the value is a list of relevant skills.
                    - 'work_experience' and 'projects' should be lists of objects, with each object structured as shown.
                    - If any piece of information is not found, use a JSON null value or an empty list where appropriate.

                    JSON Schema:
                    {{
                    "contact_information": {{
                        "name": "string",
                        "email": "string",
                        "phone": "string",
                        "linkedin": "string"
                    }},
                    "summary": "string",
                    "skills": {{
                        "Category Name": ["Skill 1", "Skill 2"]
                    }},
                    "work_experience": [
                        {{
                        "job_title": "string",
                        "company": "string",
                        "start_date": "string (YYYY-MM)",
                        "end_date": "string (YYYY-MM or Present)",
                        "responsibilities": ["string", "string", ...]
                        }}
                    ],
                    "projects": [
                        {{
                        "project_name": "string",
                        "description": "string",
                        "technologies_used": ["string", "string", ...]
                        }}
                    ],
                    "education": [
                        {{
                        "degree": "string",
                        "institution": "string",
                        "graduation_year": "string"
                        }}
                    ]
                    }}

                    Resume Text:
                    ---
                    {text}
                    ---

                    JSON Output:
                    """
            )
            raw_text = response.text
            if raw_text.startswith("```json"):
                clean_text = raw_text.strip().removeprefix("```json").removesuffix("```")
            else:
                clean_text = raw_text
            parsed_data = json.loads(clean_text)
            return parsed_data
        except Exception as e:
            logger.error(f"Error during JD parsing: {e}")
            return None