from ingestion import ingest_image
from embedding import get_embedding
from vector_db import init_index, store_vector
from search import search
from llm_answer import generate_answer
from config import EMBEDDING_DIM

import os

def ingest_pipeline(image_path):
    caption = ingest_image(image_path)
    embedding = get_embedding(caption)

    store_vector(embedding, {
        "path": image_path,
        "caption": caption
    })


def query_with_image(image_path):
    caption = ingest_image(image_path)

    print(f"\n🧠 Generated Caption:\n{caption}\n")

    results = search(caption)

    print("\n🔍 Search Results:")
    for r in results:
        print(r)

    answer = generate_answer(caption, results)

    print("\n💡 Final Answer:\n")
    print(answer)


if __name__ == "__main__":

    # ✅ Initialize FAISS
    init_index(EMBEDDING_DIM)

    # ✅ Ingest all images
    data_folder = "data"

    for file in os.listdir(data_folder):
        path = os.path.join(data_folder, file)
        ingest_pipeline(path)

    # ✅ Query with image
    query_with_image("query/cartoon.jpg")

