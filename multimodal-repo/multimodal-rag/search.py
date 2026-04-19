from embedding import get_embedding
from vector_db import search_vector
from config import TOP_K

def search(query_text):
    query_embedding = get_embedding(query_text)
    results = search_vector(query_embedding, TOP_K)
    return results