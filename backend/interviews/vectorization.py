from sentence_transformers import SentenceTransformer, util

class TextVectorization():
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
    
    def vectorize_text(self, text):
        try:
            vectorized_text = self.model.encode(text, convert_to_tensor=True)
            return vectorized_text
        except Exception as e:
            return None
    
    def similarity_check(self, text1, text2):
        try:
            similarity = util.pytorch_cos_sim(text1, text2)
            return similarity.item()
        except Exception as e:
            return None