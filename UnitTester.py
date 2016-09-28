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
    """
    def test_3scrape_with_comma_remover(self):
        print("test3")
        expected = [['001', 'Bulbasaur', 'Grass', 'Poison',
                    'http://pokemondb.net/pokedex/Bulbasaur', 'Seed Pokemon',
                    '0.71m', '6.9 kg', '001 (Red/Blue/Yellow/FireRed/'
                                       'LeafGreen)226 (Gold/Silver/Crystal)231'
                                       ' (HeartGold/SoulSilver)080 (X/Y)']]
        self.my_scraper.set_generation(0)
        self.my_scraper.web_scraper()
        actual = self.my_scraper.get_nat_dex()
        self.assertListEqual(expected, actual)
    """
    def test_4scrape_without_comma_remover(self):
        print("test3")
        expected = [['001', 'Bulbasaur', 'Grass', 'Poison',
                     'http://pokemondb.net/pokedex/Bulbasaur', 'Seed Pokemon',
                     '0.71m', '6.9 kg', '001 (Red,Blue,Yellow,FireRed,'
                     'LeafGreen)226 (Gold,Silver,Crystal)231'
                     ' (HeartGold,SoulSilver)080 (X,Y)']]
        self.my_scraper.set_generation(0)
        self.my_scraper.web_scraper()
        actual = self.my_scraper.get_nat_dex()
        self.assertListEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()

