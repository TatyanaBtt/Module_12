import unittest

import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):

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

    def test_t_1(self):
        # print('Мы в турнире')
        t_1 = rat.Tournament(90, self.runner_1, self.runner_3)
        res = t_1.start()
        self.all_results = res
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)
        print(self.all_results)

    def test_t_2(self):
        t_2 = rat.Tournament(90, self.runner_2, self.runner_3)
        res = t_2.start()
        self.all_results = res
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)
        print(self.all_results)

    def test_t_3(self):
        t_3 = rat.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = t_3.start()
        self.all_results = res
        self.assertTrue(self.all_results[max(self.all_results)] == self.runner_3)
        print(self.all_results)


if __name__ == '__main__':
    unittest.main()
