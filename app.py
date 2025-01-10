import streamlit as st
from preprocess import extract_text_from_pdf, clean_text, preprocess_text, extract_headings
from embeddings import generate_ollama_embeddings, query_embedding_ollama
from vector_search import build_faiss_index, search_faiss_index
from sentence_transformers import SentenceTransformer
import numpy as np

def chatbot(pdf_path, user_query):
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)
    chunks = preprocess_text(cleaned_text)

    chunk_embeddings = generate_ollama_embeddings(chunks)
    index = build_faiss_index(chunk_embeddings)
    query_embedding = query_embedding_ollama(user_query)

    if query_embedding is None:
        return "Error generating query embedding."

    results = search_faiss_index(index, query_embedding, chunks)
    sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
    sentences = [sentence for result in results for sentence in result.split('. ') if len(sentence) > 0]
    sentence_embeddings = sentence_model.encode(sentences)
    query_sentence_embedding = sentence_model.encode(user_query)
    similarities = np.dot(sentence_embeddings, query_sentence_embedding)
    top_indices = np.argsort(similarities)[-3:]
    top_sentences = [sentences[i] for i in top_indices]

    return " ".join(top_sentences)

def main():
    st.title("PDF Chatbot with Ollama")
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    headings = extract_headings(uploaded_file)
    st.markdown("### Extracted Headings:")
    for heading, page in headings:
                st.markdown(f"- **{heading}** (Page {page})")

    if uploaded_file:
        query = st.text_input("Ask a question:")
        
        if query:
            response = chatbot(uploaded_file, query)
            st.write("### Chatbot Response:")
            st.markdown(response)

if __name__ == "__main__":
    main()
