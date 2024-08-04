from tests_12_1 import runner as r
import unittest


class RunnerTest(unittest.TestCase):

    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r1 = r.Runner('name1')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r2 = r.Runner('name2')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r3 = r.Runner('name1')
        r4 = r.Runner('name2')
        for _ in range(10):
            r3.run()
            r4.walk()

        self.assertNotEqual(r3.distance, r4.distance)


if __name__ == '__main__':
    unittest.main()
