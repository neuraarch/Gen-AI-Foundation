# main.py
from fastapi import FastAPI
from query_rewriter import generate_sql
from db_query import run_sql
from logs import search_logs
from reasoning import generate_answer
import os

app = FastAPI()

## This is the main API endpoint that takes a user query, generates SQL, runs the query, searches logs and generates a final answer.
## query example to be put - Why are high-value orders delayed in Pune?


@app.get("/ask")
def ask(query: str):
    sql = generate_sql(query)
    db_result = run_sql(sql)
    logs = search_logs(query)
    answer = generate_answer(query, db_result, logs)

    return {
        "generated_sql": sql,
        "db_result": db_result,
        "logs": logs,
        "final_answer": answer
    }