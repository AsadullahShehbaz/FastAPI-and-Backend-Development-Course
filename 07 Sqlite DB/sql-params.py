import sqlite3

# 1.Connect to the database(It creates if it doesn't exist)
conn = sqlite3.connect("products.db")

# 2.Create a cursor object to execute SQL commands
cursor = conn.cursor()

# 3.Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        status TEXT NOT NULL
    )
''')

# Insert row in table of database
# cursor.execute('''
#     INSERT INTO products (id, name, price, stock, status)
#     VALUES (1003, 'Marse Pro', 12.99, 12, 'active')
# ''')

# Select all rows from db 
cursor.execute('SELECT * FROM products')

# Fetch all results
all_rows = cursor.fetchall()
print(all_rows)

stock = input("Enter stock value: ")
id = input("Enter id value: ")

# 0 or true
# cursor.execute('''
#     UPDATE products SET stock = :stock WHERE id = :id
# ''', {"id": id,"stock": stock })

cursor.execute('''
    UPDATE products SET stock = :stock WHERE id >= :id
''', {"id":id,"stock": stock })

# cursor.execute('DROP TABLE products')
# 4.Commit the changes and close the connection
conn.commit()

#5. Close when done
conn.close()
