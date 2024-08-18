import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

'''Удаляем пользователя с id = 6'''
# cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
count_all_users = cursor.fetchone()[0]
print(count_all_users)

cursor.execute('SELECT SUM(balance) FROM Users')
sum_all_balance = cursor.fetchone()[0]
print(sum_all_balance)

cursor.execute('SELECT AVG(balance) FROM Users')
avg_balances = cursor.fetchone()[0]
print(avg_balances)

connection.commit()
connection.close()
