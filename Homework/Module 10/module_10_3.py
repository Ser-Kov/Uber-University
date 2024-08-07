from threading import Lock
import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            count = randint(50, 500)
            self.balance += count
            sleep(0.001)
            print(f'Пополнение: {count}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            count = randint(50, 500)
            print(f'Запрос на {count}')
            if count <= self.balance:
                self.balance -= count
                sleep(0.001)
                print(f'Снятие: {count}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
            self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')