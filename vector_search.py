import faiss
import numpy as np

def build_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def search_faiss_index(index, query_embedding, chunks, k=3):
    distances, indices = index.search(np.array([query_embedding]), k)
    return [chunks[i] for i in indices[0]]
