import queue
from random import randint
import threading
from time import sleep


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
                elif table.number == len(self.tables) and table.guest is not None:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')
                else:
                    continue

    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest is not None and table.guest.is_alive() is False:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                elif table.guest is None and self.queue.empty() is False:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
