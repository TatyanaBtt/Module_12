import unittest

from runner import Runner


class RunnerTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
