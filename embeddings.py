import requests

def generate_ollama_embeddings(text_chunks, model="llama2"):
    #here we input the embeddings to the chat bot
    url = "http://localhost:11434/api/embeddings"
    embeddings = []

    for chunk in text_chunks:
        payload = {"model": model, "input": chunk}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            embeddings.append(response.json()["embedding"])
        else:
            print(f"Error: {response.status_code} - {response.text}")
    return embeddings

def query_embedding_ollama(query, model="llama2"):
    #here the chatbot processes the enquiry
    url = "http://localhost:11434/api/embeddings"
    payload = {"model": model, "input": query}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["embedding"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
