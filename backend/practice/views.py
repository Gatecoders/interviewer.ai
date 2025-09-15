from interviews.text_extractor import TextExtractor
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from interviews.vectorization import TextVectorization
from interviews.vector_store import VectorStore
from interviews.parser import JdParser, ResumeParser
import logging
import os

log_path = os.path.join(os.path.dirname(__file__), '..', 'debug.log')
log_dir = os.path.dirname(os.path.abspath(log_path))
os.makedirs(log_dir, exist_ok=True)

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Avoid duplicate handlers if this module is reloaded
if not logger.handlers:
    # Create file handler
    file_handler = logging.FileHandler(os.path.abspath(log_path))
    file_handler.setLevel(logging.DEBUG)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # or logging.INFO for less noise

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def text_extraction_api(request):
    resume_file = request.FILES.get('resume')
    job_description_file = request.FILES.get('job_description')
    if not resume_file or not job_description_file:
        logger.error("Both resume and job description files are required.")
        return Response({"error": "Both resume and job description files are required."}, status=400)
    
    try:
        text_jd = TextExtractor(job_description_file).extract_text()
        text_resume = TextExtractor(resume_file).extract_text()
        if not text_jd or not text_resume:
            logger.error("No text extracted from the files.")
            return Response({"error": "No text extracted from the files."}, status=400)
    except Exception as e:
        logger.error(f"Error during text extraction: {e}")
        return Response({"error": "Error occurred while extracting text from the files."}, status=500)
    
    try:
        jd_data = JdParser().jd_parser(text_jd)
        resume_data = ResumeParser().resume_parser(text_resume)
        if jd_data is None or resume_data is None:
            logger.error("Error occurred while parsing the job description or resume.")
            return Response({"error": "Error occurred while parsing the job description or resume."}, status=500)
        jd_skills = jd_data.get('required_skills', 'None')
        resume_skills = resume_data.get('skills', 'None')
        candidate_skills = [skill for category in resume_skills.values() for skill in category]
    except Exception as e:
        logger.error(f"Error during parsing: {e}")
        return Response({"error": "Error occurred while parsing the text."}, status=500)
    
    try:
        vectorization = TextVectorization()
        vectorized_jd_skills = vectorization.vectorize_text(jd_skills)
        vectorized_resume_skills = vectorization.vectorize_text(candidate_skills)
        if vectorized_jd_skills is None or vectorized_resume_skills is None:
            logger.error("Error occurred while vectorizing the text.")
            raise ValueError("Vectorization failed")
    except Exception as e:
        logger.error(f"Error during text vectorization: {e}")
        return Response({"error": "Error occurred while vectorizing the text."}, status=500)
    
    try:
        similarity = vectorization.similarity_check(vectorized_jd_skills, vectorized_resume_skills)
        if similarity is None:
            logger.error("Error occurred while calculating similarity.")
            return Response({"error": "Error occurred while calculating similarity."}, status=500)
        return Response({
            "similarity_score": similarity,
            "jd_data": jd_data,
            "resume_data": resume_data
        }, status=200)
    except Exception as e:
        logger.error(f"Error during similarity calculation: {e}")
        return Response({"error": "Error occurred while calculating similarity."}, status=500)