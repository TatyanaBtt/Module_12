import unittest

from runner import Runner

import runner_and_tournament as rat


class RunnerTest(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        num_1 = Runner('Vasya')
        num_1.walk()
        num_1.walk()
        num_1.walk()
        num_1.walk()
        num_1.walk()
        num_1.walk()
        num_1.walk()
        num_1.walk()
        num_1.walk()
        num_1.walk()
        self.assertEqual(num_1.distance, 50)

    def test_run(self):
        num_2 = Runner('Peter')
        num_2.run()
        num_2.run()
        num_2.run()
        num_2.run()
        num_2.run()
        num_2.run()
        num_2.run()
        num_2.run()
        num_2.run()
        num_2.run()
        self.assertEqual(num_2.distance, 100)

    def test_challenge(self):
        num_3 = Runner('John')
        num_4 = Runner('Mary')
        num_3.run()
        num_3.run()
        num_3.run()
        num_3.run()
        num_3.run()
        num_3.run()
        num_3.run()
        num_3.run()
        num_3.run()
        num_3.run()
        num_4.walk()
        num_4.walk()
        num_4.walk()
        num_4.walk()
        num_4.walk()
        num_4.walk()
        num_4.walk()
        num_4.walk()
        num_4.walk()
        num_4.walk()
        self.assertNotEqual(num_3.distance, num_4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = rat.Runner('Усэйн', 10)
        self.runner_2 = rat.Runner('Андрей', 9)
        self.runner_3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # print(cls.all_results)
        for key, value in cls.all_results.items():
            print(key, value)
    @unittest.skip('Тесты в этом кейсе заморожены')
    def test_t_1(self):
        t_1 = rat.Tournament(90, self.runner_1, self.runner_3)
        res = t_1.start()
        self.all_results = res
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)
        print(self.all_results)

    @unittest.skip('Тесты в этом кейсе заморожены')
    def test_t_2(self):
        t_2 = rat.Tournament(90, self.runner_2, self.runner_3)
        res = t_2.start()
        self.all_results = res
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)
        print(self.all_results)

    @unittest.skip('Тесты в этом кейсе заморожены')
    def test_t_3(self):
        t_3 = rat.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = t_3.start()
        self.all_results = res
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)
        print(self.all_results)


if __name__ == '__main__':
    unittest.main()
