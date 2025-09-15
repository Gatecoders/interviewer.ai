from .embedding_models import EmbedingModels
import logging
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)

class TextVectorization():
    def __init__(self, model_name='models/embedding-001'):
        self.model = EmbedingModels(model_name)
    
    def vectorize_text_google(self, text):
        try:
            response = self.model.google_embed(text)
            logger.info("Text successfully vectorized using SentenceTransformer.")
        except Exception as e:
            logger.error(f"Error during SentenceTransformer: {e}.")
            return None
        if response and len(response) > 0:
            vector = response[0]['values']
        return vector
    

    def vectorize_text(self, text):
        try:
            vector = self.model.sentence_transformer_embed(text)
            logger.info("Text successfully vectorized using SentenceTransformer.")
        except Exception as e:
            logger.error(f"Error during SentenceTransformer: {e}.")
            return None
        return vector
        
    
    def similarity_check(self, vector1, vector2)-> float:
        #Move tensors from GPU ('mps') to the CPU
        vector1 = vector1.cpu()
        vector2 = vector2.cpu()

        #Convert the CPU tensors to NumPy arrays
        # Using .detach() is a good practice to remove them from the computation graph
        vec1 = vector1.detach().numpy()
        vec2 = vector2.detach().numpy()

        # Compute the similarity matrix using scikit-learn
        similarity_matrix = cosine_similarity(vec1, vec2)

        #Aggregate the matrix into a single, meaningful score
        max_similarity_per_skill = np.max(similarity_matrix, axis=1)

        #Calculate the average of these best-match scores.
        average_score = np.mean(max_similarity_per_skill)
        
        return float(average_score)