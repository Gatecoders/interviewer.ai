import chromadb
import logging

logger = logging.getLogger(__name__)

class VectorStore():
    def __init__(self, collection_name: str):
        self.client = chromadb.EphemeralClient()
        self.collection = self.client.get_or_create_collection(name=collection_name)
    
    def add_vector(self, vector):
        try:
            self.collection.add(
                ids = [vector.get('id', 'unknown_id')],
                documents=[vector.get('text', '')], 
                embeddings=[vector.get('vectorized_skills')],
                metadatas=[{
                    'company_name': vector.get('company_name', 'Unknown'),
                    'skills': vector.get('skills', 'None'),
                    'role': vector.get('role', 'None'),
                    'responsibilities': vector.get('responsibilities', 'None'),
                }]

            )
            return True
        except Exception as e:
            logger.error(f"Error adding vector to store: {e}")
            return False