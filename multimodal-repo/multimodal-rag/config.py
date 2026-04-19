from openai import OpenAI

client = OpenAI()

EMBEDDING_MODEL = "text-embedding-3-large"
VISION_MODEL = "gpt-4.1-mini"

EMBEDDING_DIM = 3072
TOP_K = 3