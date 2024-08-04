import unittest
from runner_and_tournament import runner_and_tournament_teset as r1
from tests_12_1 import runner_test as r2

# import tests_12_1.runner_test as RunnerTest


runTestST = unittest.TestSuite()

runTestST.addTest(unittest.TestLoader().loadTestsFromTestCase(r1.TournamentTes))
runTestST.addTest(unittest.TestLoader().loadTestsFromTestCase(r2.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runTestST)