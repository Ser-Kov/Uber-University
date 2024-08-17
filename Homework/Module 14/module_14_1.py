import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

'''Создаем столбцы со значениями'''
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', 1000))

'''Обновляем баланс каждого второй пользователя на 500'''
list_id = [i for i in range(1, 11)]
list_id_for_step_2 = list_id[::2]
for i in list_id_for_step_2:
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))

'''Удаляем каждого 3-го пользоваеля'''
list_id = [i for i in range(1, 11)]
list_id_for_step_3 = list_id[::3]
for i in list_id_for_step_3:
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

'''Осуществляем выборку пользователей, у кого возраст не равен 60, и выводим данные в консоль'''
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')


connection.commit()
connection.close()

