import unittest
import tests_12_1, tests_12_2


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_obj_1 = tests_12_1.Runner('Sarah')
        for i in range(10):
            test_obj_1.walk()
        self.assertEqual(test_obj_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_obj_2 = tests_12_1.Runner('John')
        for i in range(10):
            test_obj_2.run()
        self.assertEqual(test_obj_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_obj_3 = tests_12_1.Runner('Maria')
        test_obj_4 = tests_12_1.Runner('Alex')
        for i in range(10):
            test_obj_3.run()
            test_obj_4.walk()
        self.assertNotEqual(test_obj_3.distance, test_obj_4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.test_obj_1 = tests_12_2.Runner('Усейн', 10)
        self.test_obj_2 = tests_12_2.Runner('Андрей', 9)
        self.test_obj_3 = tests_12_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_racing_1(self):
        Useyn_Nick = tests_12_2.Tournament(90, self.test_obj_1, self.test_obj_3)
        result_racing = Useyn_Nick.start()
        self.all_results.append(result_racing)
        self.assertTrue(result_racing[max(result_racing.keys())], self.test_obj_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_racing_2(self):
        Andrey_Nick = tests_12_2.Tournament(90, self.test_obj_2, self.test_obj_3)
        result_racing = Andrey_Nick.start()
        self.all_results.append(result_racing)
        self.assertTrue(result_racing[max(result_racing.keys())], self.test_obj_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_racing_3(self):
        Useyn_Andrey_Nick = tests_12_2.Tournament(90, self.test_obj_1, self.test_obj_2,
                                                  self.test_obj_3)
        result_racing = Useyn_Andrey_Nick.start()
        self.all_results.append(result_racing)
        self.assertTrue(result_racing[max(result_racing.keys())], self.test_obj_3.name)

