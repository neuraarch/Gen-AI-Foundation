from connector import generate_llm_response

def generate_answer(query, results):
    context = "\n".join([r["caption"] for r in results])

    prompt = f"""
You are a car assistant.

Context:
{context}

User query:
{query}

Explain:
1. What the warning means
2. Is it dangerous
3. What should user do
"""

    return generate_llm_response(prompt)