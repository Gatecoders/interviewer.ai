import chromadb

class VectorStore():
    def __init__(self, collection_name: str):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name=collection_name)
    
    def add_vector(self, vector):
        try:
            self.collection.add(documents=[vector['text']], embeddings=[vector['embedding']])
            return True
        except Exception as e:
            print(f"Error adding vector: {e}")
            return False