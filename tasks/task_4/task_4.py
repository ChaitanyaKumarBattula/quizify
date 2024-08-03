# embedding_client.py

from langchain_google_vertexai import VertexAIEmbeddings
import streamlit as st

class EmbeddingClient:
    """
    Initialize the EmbeddingClient class to connect to Google Cloud's VertexAI for text embeddings.
    """
    
    def __init__(self, model_name, project, location):
        self.client = VertexAIEmbeddings(
            model_name = model_name,
            project = project,
            location = location

        )
        
    def embed_query(self, query):
        """
        Uses the embedding client to retrieve embeddings for the given query.
        """
        vectors = self.client.embed_query(query)
        return vectors
    
    def embed_documents(self, documents):
        """
        Retrieve embeddings for multiple documents.
        """
        try:
            return self.client.embed_documents(documents)
        except AttributeError:
            print("Method embed_documents not defined for the client.")
            return None

if __name__ == "__main__":
    model_name = "textembedding-gecko@003"
    project = "gemini-quizzify-426812"
    location = "us-central1"

    embedding_client = EmbeddingClient(model_name, project, location)
    vectors = embedding_client.embed_query("Hello World!")
    if vectors:
        st.write(vectors)
        st.success("Successfully retrieved and displayed the embeddings.")
        
