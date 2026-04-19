import faiss
import numpy as np

index = None
data_store = []

def init_index(dimension):
    global index
    index = faiss.IndexFlatL2(dimension)

## Store vector and metadata
def store_vector(vector, metadata):
    global index, data_store

    vec = np.array([vector]).astype("float32")
    index.add(vec)
    data_store.append(metadata)

## Search for similar vectors
def search_vector(query_vector, top_k):
    global index, data_store

    query = np.array([query_vector]).astype("float32")

    top_k = min(top_k, len(data_store))

    D, I = index.search(query, top_k)

    results = []

    for idx, dist in zip(I[0], D[0]):
        if idx < len(data_store):

            confidence = 1 / (1 + float(dist))

            item = data_store[idx]

            results.append({
                **item,
                "distance": float(dist),
                "confidence": confidence
            })

    return results