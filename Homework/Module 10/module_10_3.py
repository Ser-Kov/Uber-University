from threading import Lock, Thread
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            count = randint(50, 500)
            with self.lock:
                self.balance += count
                sleep(0.001)
                print(f'Пополнение: {count}. Баланс: {self.balance}.')

    def take(self):
        for i in range(100):
            count = randint(50, 500)
            print(f'Запрос на {count}')
            with self.lock:
                if count <= self.balance:
                    self.balance -= count
                    sleep(0.001)
                    print(f'Снятие: {count}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')