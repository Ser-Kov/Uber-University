import logging, unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.is_frozen = True

    # @unittest.skipIf()
    def test_walk(self):
        try:
            test_obj_1 = Runner('Sarah')
            for i in range(10):
                test_obj_1.walk()
            self.assertEqual(test_obj_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            test_obj_2 = Runner('John')
            for i in range(10):
                test_obj_2.run()
            self.assertEqual(test_obj_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        test_obj_3 = Runner('Maria')
        test_obj_4 = Runner('Alex')
        for i in range(10):
            test_obj_3.run()
            test_obj_4.walk()
        self.assertNotEqual(test_obj_3.distance, test_obj_4.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(levelname)s | %(message)s')

    first = Runner('Вося', 10)
    second = Runner('Илья', 5)
    third = Runner('Арсен', 10)

    t = Tournament(101, first, second)
    print(t.start())