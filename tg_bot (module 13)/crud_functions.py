import sqlite3


connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')


initiate_db()

# for i in range(10, 14):
#     cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
#                    (i, f'Iphone {i}', i, i * 100))


def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    connection.commit()
    return products


for product in get_all_products():
    print(product)

connection.commit()
