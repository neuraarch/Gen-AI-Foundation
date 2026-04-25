import sqlite3

## This file contains functions to initialize the database and run SQL queries.
## database order.db is created on the fly in file db.py and 
## it has a single table called orders with columns id, city, status, order_value and delay_reason. The function init_db() creates the database and inserts dummy data for testing purposes. The function run_sql(query) takes an SQL query as input and returns the results of the query execution.
def run_sql(query):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()
    except Exception as e:
        results = str(e)

    conn.close()
    return results