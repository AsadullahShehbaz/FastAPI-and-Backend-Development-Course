# Lecture 8.1 - Context managers (applied to a database class)
import sqlite3
from contextlib import contextmanager


class Database:
    def connect_to_db(self):
        self.conn = sqlite3.connect(":memory:")
        self.cur = self.conn.cursor()
        print("connected to the database")

    def create_table(self):
        self.cur.execute(
            "CREATE TABLE product (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER)"
        )
        self.cur.execute("INSERT INTO product VALUES (1001, 'Wireless Mouse', 18.99, 42)")
        self.cur.execute("INSERT INTO product VALUES (1002, 'Mechanical Keyboard', 64.99, 18)")

    def get(self, id: int):
        self.cur.execute("SELECT * FROM product WHERE id = ?", (id,))
        return self.cur.fetchone()

    def close(self):
        print("...connection closed")
        self.conn.close()

    # Approach 1: a class becomes a context manager with two dunder methods
    def __enter__(self):
        print("enter the context")
        self.connect_to_db()
        self.create_table()
        return self                     # without this, "as db" would be None

    def __exit__(self, *args):          # extra args = error info, unused here
        print("exiting the context")
        self.close()


# Usage 1 - same idea as:  with open("file.txt") as f:
with Database() as db:
    print(db.get(1001))
    print(db.get(1002))
# connection is closed automatically here


# Generators: yield PAUSES the function, next() RESUMES it
def gen_table_of_five():
    for n in [5, 10, 15, 20, 25]:
        yield n

gen = gen_table_of_five()
print(next(gen), next(gen))             # 5 10
for number in gen_table_of_five():
    print(number, end=" ")
print()


# Approach 2: a generator function + @contextmanager
# (works even for classes you cannot edit)
@contextmanager
def managed_db():
    db = Database()
    db.connect_to_db()                  # setup
    db.create_table()
    try:
        yield db                        # hand over to the with-block and wait
    finally:
        db.close()                      # teardown - runs even if the block fails


with managed_db() as db:
    print(db.get(1001))
