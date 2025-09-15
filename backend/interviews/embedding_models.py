from sentence_transformers import SentenceTransformer, util
from google import genai
from google.genai import types
from dotenv import load_dotenv
import logging
import os

load_dotenv()

class EmbedingModels:
    def __init__(self, google_model_name='models/embedding-001'):
        self.google_model_name = google_model_name
        self.sentence_transformer_model_name = 'all-MiniLM-L6-v2'
        self.client = genai.Client()
        
    def google_embed(self, text):
        response = self.client.models.embed_content(
            model=self.google_model_name,
            contents=text,
            config=types.EmbedContentConfig(output_dimensionality=768)
        )
        return response.embeddings
    
    def sentence_transformer_embed(self, text):
        model = SentenceTransformer(self.sentence_transformer_model_name)
        embeddings = model.encode(text, convert_to_tensor=True)
        return embeddings