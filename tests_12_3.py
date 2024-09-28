import unittest
from unittest import TestCase
from test12 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        x = Runner('Mark')
        for i in range(10):
            x.walk()
        self.assertEqual(x.distance, 50, f'{x.name} должен пройти 50 метров, а прошел {x.distance}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        y = Runner('Ugor')
        for i in range(10):
            y.run()
        self.assertEqual(y.distance, 100, f'{y.name} должен пробежать 100 метров, а пробежал {y.distance}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        x = Runner('Mark')
        y = Runner('Ugor')
        for i in range(10):
            x.walk()
            y.run()
        self.assertNotEqual(x.distance, y.distance)


class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.first = Runner('Усэйн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tour(self):
        tournament = Tournament(90, self.first, self.third)
        res = tournament.start()
        TournamentTest.all_result.append(res)
        self.assertTrue(res[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tour(self):
        tournament = Tournament(90, self.second, self.third)
        res = tournament.start()
        TournamentTest.all_result.append(res)
        self.assertTrue(res[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tour(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        res = tournament.start()
        TournamentTest.all_result.append(res)
        self.assertTrue(res[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for k, v in enumerate(cls.all_results):
            print(f'{k+1}: {v}')



