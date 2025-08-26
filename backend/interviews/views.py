from text_extractor import TextExtractor
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from vectorization import TextVectorization
from vector_store import VectorStore

@api_view['POST']
@parser_classes([MultiPartParser, FormParser])
def text_extraction_api(request):
    document_type = request.data.get('document_type')
    uploaded_file = request.FILES.get('document')
    if not uploaded_file:
        return Response({"error": "No file uploaded."}, status=400)
    try:
        text = TextExtractor(uploaded_file).extract_text()
        if not text:
            return Response({"error": "No text extracted from the file."}, status=400)
        
        try:
            vectorization = TextVectorization()
            vectorized_text = vectorization.vectorize_text(text)
            if vectorized_text is None:
                return Response({"error": "No text to vectorize."}, status=500)
        except Exception as e:
            return Response({"error": "Error occurred while vectorizing the text."}, status=500)
        
        if document_type == 'job_description':
            VectorStore(collection_name='job_descriptions').add_vector({
                'text': text,
                'embedding': vectorized_text
            })
        else:
            pass

    except Exception as e:
        return Response({"error": str(e)}, status=400)

