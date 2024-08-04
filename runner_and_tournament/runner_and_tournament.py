from runner_and_tournament import runner_and_tournament as run
import unittest


class TournamentTes(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print(i)



    def setUp(self):
        self.usein = run.Runner(name='Усэйн', speed=10)
        self.andrie = run.Runner(name='Андрей', speed=9)
        self.nick = run.Runner(name='Ник', speed=3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        run1 = run.Tournament(90, self.usein, self.nick)
        result = run1.start()
        self.all_results['test1'] = {a: b.name for a, b in result.items()}
        self.assertEqual(result[2], self.nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        run1 = run.Tournament(90, self.andrie, self.nick)
        result = run1.start()
        self.all_results['test2'] = {a: b.name for a, b in result.items()}
        self.assertEqual(result[2], self.nick.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        run1 = run.Tournament(90, self.usein, self.andrie, self.nick)
        result = run1.start()
        self.all_results['test3'] = {a: b.name for a, b in result.items()}
        self.assertEqual(result[3], self.nick.name)



if __name__ == '__main__':
    unittest.main()








