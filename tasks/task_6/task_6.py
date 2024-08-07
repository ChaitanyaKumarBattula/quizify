import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator

if __name__ == "__main__":
    st.header("Quizzify")

    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "gemini-quizzify-426812",
        "location": "us-central1"
    }
    
    screen = st.empty() # Screen 1, ingest documents
    with screen.container():
        # st.header("Quizzify")
        

        # 1) Initalize DocumentProcessor and Ingest Documents from Task 3
        processor = DocumentProcessor()
        processor.ingest_documents()

        # 2) Initalize the EmbeddingClient from Task 4 with embed config
        embedding_client = EmbeddingClient(**embed_config)

        # 3) Initialize the ChromaCollectionCreator from Task 5
        chroma_creator = ChromaCollectionCreator(processor, embedding_client)

        

        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            

            # 4) Use streamlit widgets to capture the user's input
            quiz_topic = st.text_input("Enter the quiz topic:")

            # 4) for the quiz topic and the desired number of questions
            num_questions = st.number_input("Number of Questions", min_value=1, max_value=50, value=10)

            
            document = None
            
            submitted = st.form_submit_button("Generate a Quiz!")
            if submitted:

                chroma_creator.create_chroma_collection()
                    
                # Uncomment the following lines to test the query_chroma_collection() method
                # document = chroma_creator.query_chroma_collection(quiz_topic) 
                
    if document:
        screen.empty() # Screen 2
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)