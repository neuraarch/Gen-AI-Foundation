# reasoning.py
from chat_config import client, CHAT_MODEL

## This function takes the user query, SQL result and logs as input and generates a clear explanation of the reason using the OpenAI API.
def generate_answer(user_query, sql_result, logs):
    prompt = f"""
    User question: {user_query}

    SQL Data:
    {sql_result}

    Logs:
    {logs}

    Analyze and explain the reason clearly.
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content