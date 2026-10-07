# A SQLite database is just a FILE (created if missing)
import sqlite3

connection = sqlite3.connect("products_basics.db")
# The cursor is what executes queries and fetches rows
cursor = connection.cursor()

# IF NOT EXISTS -> running the file twice does not crash
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    stock INTEGER
)
""")