import sqlite3


connection = sqlite3.connect('users.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')


initiate_db()


id_user = 1


def add_user(username, email, age):
    global id_user
    cursor.execute(f'INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)',
                   (id_user, username, email, age, 1000))
    id_user += 1
    connection.commit()


def is_included(username):
    if cursor.execute('SELECT username FROM Users').fetchone() is None:
        return False
    else:
        users = cursor.execute('SELECT username FROM Users').fetchone()
        return True if username in users else False


connection.commit()
