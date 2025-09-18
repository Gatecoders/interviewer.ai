from interviews.interviewer import AIAssistedInterviewer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai


@api_view(['POST'])
def start_interview(request):
    """
    Initializes an interview session based on JD and resume data.
    """
    try:
        jd_data = request.data.get('jd_data')
        resume_data = request.data.get('resume_data')
        interview_type = request.data.get('interview_type', 'Technical')
        difficulty_level = request.data.get('difficulty_level', 'Medium')

        if not jd_data or not resume_data:
            return Response({"error": "Both 'jd_data' and 'resume_data' are required."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        interviewer = AIAssistedInterviewer(jd_data, resume_data, interview_type, difficulty_level)
        first_question = interviewer.start_interview()
        # Convert history to a JSON-serializable format before saving
        serializable_history = [
            {'role': msg.role, 'parts': [part.text for part in msg.parts]}
            for msg in interviewer.chat.history
        ]
        request.session['interview_history'] = serializable_history

        return Response({"question": first_question}, 
                        status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def respond_to_interview(request):
    """
    Processes a user's answer and returns the AI's next question.
    """
    import pdb; pdb.set_trace()
    history = request.session.get('interview_history')
    user_answer = request.data.get('answer')

    if not history:
        return Response(
            {"error": "Interview session not found. Please start a new interview."},
            status=status.HTTP_400_BAD_REQUEST
        )
    if not user_answer:
         return Response({"error": "Answer is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        interviewer = AIAssistedInterviewer(history=history)
        next_question = interviewer.process_candidate_response(user_answer)
        # Convert the updated history before saving it back
        serializable_history = [
            {'role': msg.role, 'parts': [part.text for part in msg.parts]}
            for msg in interviewer.chat.history
        ]
        request.session['interview_history'] = serializable_history
        return Response({"question": next_question}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)