import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_obj_1 = Runner('Sarah')
        for i in range(10):
            test_obj_1.walk()
        self.assertEqual(test_obj_1.distance, 50)

    def test_run(self):
        test_obj_2 = Runner('John')
        for i in range(10):
            test_obj_2.run()
        self.assertEqual(test_obj_2.distance, 100)

    def test_challenge(self):
        test_obj_3 = Runner('Maria')
        test_obj_4 = Runner('Alex')
        for i in range(10):
            test_obj_3.run()
            test_obj_4.walk()
        self.assertNotEqual(test_obj_3.distance, test_obj_4.distance)


if __name__ == '__main__':
    unittest.main()



