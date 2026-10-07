from contextlib import contextmanager
import sqlite3

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
        return self
    # without this, "as db" would be None
    def __exit__(self, *args):          
        print("exiting the context")
        self.close()

with Database() as db:
    print(db.get(1001))
    print(db.get(1002)) 


@contextmanager
def managed_db():
    db = Database()
    db.connect_to_db()                  
    db.create_table()
    try:
        yield db                        
    finally:
        db.close()                      
with managed_db() as db:
    print(db.get(1001))