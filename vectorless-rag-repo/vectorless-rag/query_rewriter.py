from chat_config import client, CHAT_MODEL

## This function takes a user query as input and generates an SQL query using the OpenAI API.

def generate_sql(user_query):

    prompt = f"""
    Convert the following user query into SQL.

    User Query: {user_query}

    Table: orders(id, city, status, order_value, delay_reason)

    Only return raw SQL query. Do NOT include markdown, backticks, or explanations.
    """
    
  

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    sql = response.choices[0].message.content.strip()

    #  CLEANUP STEP (critical)
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql