import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.test_obj_1 = Runner('Усейн', 10)
        self.test_obj_2 = Runner('Андрей', 9)
        self.test_obj_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    def test_racing_1(self):
        Useyn_Nick = Tournament(90, self.test_obj_1, self.test_obj_3)
        result_racing = Useyn_Nick.start()
        self.all_results.append(result_racing)
        self.assertTrue(result_racing[max(result_racing.keys())], self.test_obj_3.name)

    def test_racing_2(self):
        Andrey_Nick = Tournament(90, self.test_obj_2, self.test_obj_3)
        result_racing = Andrey_Nick.start()
        self.all_results.append(result_racing)
        self.assertTrue(result_racing[max(result_racing.keys())], self.test_obj_3.name)

    def test_racing_3(self):
        Useyn_Andrey_Nick = Tournament(90, self.test_obj_1, self.test_obj_2, self.test_obj_3)
        result_racing = Useyn_Andrey_Nick.start()
        self.all_results.append(result_racing)
        self.assertTrue(result_racing[max(result_racing.keys())], self.test_obj_3.name)


if __name__ == '__main__':
    unittest.main()