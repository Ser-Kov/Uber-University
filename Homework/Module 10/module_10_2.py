from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        count_enemies = 100
        days_fight = 0
        print(f'{self.name}, на нас напали!')
        sleep(1)
        for i in range(count_enemies // self.power):
            count_enemies -= self.power
            print(f'{self.name} сражается {i + 1} день, осталось {count_enemies} воинов.')
            days_fight += 1
            sleep(1)
        print(f'{self.name} одержал победу спустя {days_fight} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')