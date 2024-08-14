import unittest
import tests_12_1, tests_12_2, tests_12_3


module_12_TS_1 = unittest.TestSuite()
module_12_TS_1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
module_12_TS_1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(module_12_TS_1)

module_12_TS_2 = unittest.TestSuite()
module_12_TS_2.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
module_12_TS_2.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner.run(module_12_TS_2)