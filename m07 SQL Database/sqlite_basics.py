# Lecture 7.3 - SQLite: connection, cursor, create a table
import sqlite3

# A SQLite database is just a FILE (created if missing)
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

# Always close the connection when you are done
connection.close()
