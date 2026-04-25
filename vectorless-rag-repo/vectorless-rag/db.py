import sqlite3

## on the fly db creation and data insertion for testing purposes
## name of the db is orders.db and it has a single table called orders with columns id, city, status, order_value and delay_reason

def init_db():
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER,
        city TEXT,
        status TEXT,
        order_value INTEGER,
        delay_reason TEXT
    )
    """)
## dummy data for testing

    data = [
        (1, "Pune", "delayed", 15000, "warehouse backlog"),
        (2, "Pune", "delayed", 20000, "courier shortage"),
        (3, "Mumbai", "on_time", 12000, "none"),
        (4, "Pune", "delayed", 18000, "warehouse backlog"),
    ]

    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()