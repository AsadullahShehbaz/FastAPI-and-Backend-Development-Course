from contextlib import contextmanager
import sqlite3
from typing import Any

from app.schema.models import ProductCreate, ProductUpdate

class Database:

    # Initialize DB
    def connect_to_db(self):
        self.conn = sqlite3.connect("products.db",check_same_thread=False)
        self.cur = self.conn.cursor()
        

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')

    def create(self,product: ProductCreate):

        # Find the next id 
        self.cur.execute('SELECT MAX(id) FROM products')
        result = self.cur.fetchone() 
        new_id = (result[0] or 0) + 1

        self.cur.execute('''
        INSERT INTO products (id, name, price, stock)
        VALUES (:id, :name, :price, :stock)
    ''', {
        'id': new_id,
        **product.model_dump()
    })

        self.conn.commit()
        return new_id

    def get(self,id: int)-> dict[str,Any] | None:
        self.cur.execute('SELECT * FROM products WHERE id = :id', {'id': id})
        result = self.cur.fetchone()
        
        return {
                'id': result[0],
                'name': result[1],
                'price': result[2],
                'stock': result[3]
            } if result else None

    def update(self,id: int, product_update: ProductUpdate):

        data = product_update.model_dump(exclude_none=True)
        set_clause = ','.join(f"{key}=:{key}" for key in data)
        
        self.cur.execute('''
            UPDATE products
            SET ''' + set_clause + '''
            WHERE id = :id
        ''', {
            'id': id,
            **data
        })
        self.conn.commit()

        return self.get(id)

    def delete(self,id: int):
        self.cur.execute('DELETE FROM products WHERE id = :id', {'id': id})
        self.conn.commit()

    def close(self):
        self.conn.close()

    # def __enter__(self):
    #     self.connect_to_db()
    #     self.create_table()
    #     return self 

    # def __exit__(self, *args):
    #     self.close()



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
    print(db.get(1))


