import unittest
from rt_with_exception import Runner
import logging


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            num_1 = Runner('Vasya', speed=-5)
            logging.info('test_walk" выполнен успешно')
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
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            num_2 = Runner(5)
            logging.info('test_run" выполнен успешно')
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
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        try:
            num_3 = Runner('John')
            num_4 = Runner('Mary')
            logging.info('test_challenge" выполнен успешно')
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
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

if __name__ == '__main__':
    unittest.main()
