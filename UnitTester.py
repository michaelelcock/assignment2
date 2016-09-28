import unittest
from Controller import Controller
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from IO import IO
from command import Command
import pokemon_scraper
import sys
import os


class UnitTesting(unittest.TestCase):

    def setUp(self):
        print("testing")
        self.my_scraper = PokemonScraper(Formatter)
        self.c = Controller(self.my_scraper, IO)

    def tearDown(self):
        pass
    """
    def test_1height__imp_remover(self):
        print("test1")
        expected = "0.71m"
        actual = Formatter.height_imp_remover("2′4″ (0.71m)", "m")
        self.assertEqual(expected, actual)
    """
    def test_1height__imp_remover(self):
        print("test1")
        expected = "0.71m"
        actual = Formatter.height_weight_imp_remover("2′4″ (0.71m)", "m")
        self.assertEqual(expected, actual)
    """
    def test_2weight_imp_remover(self):
        print("test2")
        expected = "6.9 kg"
        actual = Formatter.weight_imp_remover("15.2 lbs (6.9 kg)"
                                                     , " kg")
        self.assertEqual(expected, actual)
    """
    def test_2weight_imp_remover(self):
        print("test2")
        expected = "6.9 kg"
        actual = Formatter.height_weight_imp_remover("15.2 lbs (6.9 kg)"
                                                     , " kg")
        self.assertEqual(expected, actual)

    def test_3comma_remover(self):
        print("test3")
        expected = "(Red/Blue/Yellow/FireRed/LeafGreen)"
        actual = Formatter.comma_remover("(Red,Blue,Yellow,FireRed,LeafGreen)")
        self.assertEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()

