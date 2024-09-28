import unittest
import tests_12_3

#Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
#Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
#Создайте объект класса TextTestRunner, с аргументом verbosity=2.

s1 = unittest.TestSuite()
s1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
s1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(s1)

