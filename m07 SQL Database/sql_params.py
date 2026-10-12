# Lecture 7.5 - Passing values into SQL safely (and SQL injection)
import sqlite3

connection = sqlite3.connect(":memory:")       # temporary database, lives in RAM
cursor = connection.cursor()
cursor.execute("CREATE TABLE product (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER)")
cursor.executemany(
    "INSERT INTO product VALUES (?, ?, ?, ?)",
    [(1001, "Wireless Mouse", 18.99, 42),
     (1002, "Mechanical Keyboard", 64.99, 18),
     (1003, "USB-C Hub", 29.99, 35)],
)
connection.commit()


def stocks() -> list:
    cursor.execute("SELECT id, stock FROM product")
    return cursor.fetchall()


# BAD: f-string. The "id" text becomes part of the SQL code!
product_id = "0 or true"                 # a malicious "id"
cursor.execute(f"UPDATE product SET stock = 0 WHERE id = {product_id}")
print("after injection:", stocks())      # EVERY row now has stock 0

# put the data back
cursor.execute("UPDATE product SET stock = 10")

# GOOD 1: positional placeholders "?"  + tuple (order matters)
cursor.execute(
    "UPDATE product SET stock = ? WHERE id = ?",
    (25, 1001),
)

# GOOD 2: named placeholders ":name" + dict (order does not matter)
cursor.execute(
    "UPDATE product SET stock = :stock WHERE id = :id",
    {"stock": 99, "id": 1002},
)

# The injection attempt is now just a value that matches nothing
cursor.execute(
    "UPDATE product SET stock = :stock WHERE id = :id",
    {"stock": 0, "id": "0 or true"},
)
print("after safe queries:", stocks())

# WHERE also supports > < >= <=
cursor.execute(
    "UPDATE product SET stock = :stock WHERE id > :id",
    {"stock": 5, "id": 1001},
)
connection.commit()
print("final:", stocks())
connection.close()
