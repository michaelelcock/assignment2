import unittest
from Controller import Controller
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from IO import IO
from command import Command
import pokemon_scraper


class UnitTesting(unittest.TestCase):

    def setUp(self):
        print("testing")

    def tearDown(self):
        pass

    def test_height__imp_remover(self):
        expected = "0.71m"
        actual = Formatter.height_weight_imp_remover("2′4″ (0.71m)", "m")
        self.assertEqual(expected, actual)

    def test_weight_imp_remover(self):
        expected = "6.9 kg"
        actual = Formatter.height_weight_imp_remover("15.2 lbs (6.9 kg)",
                                                     " kg")
        self.assertEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()

