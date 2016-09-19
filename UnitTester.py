import unittest
from Controller import Controller
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from IO import IO
from command import Command
import pokemon_scraper


class UnitTesting(unittest.TestCase):
    """
    @classmethod
    def setUpClass(cls):
        super(UnitTesting, cls).setUpClass()
        cls.my_controller = Controller.(

        )
    """

    def setUp(self):
        print("testing")

    def tearDown(self):
        pass

    def test_weight_imp_remover(self):
        expected = "6.9 kg"
        actual = Formatter.weight_imp_remover("15.2 lbs (6.9 kg)")
        self.assertEqual(expected, actual)

    def test_height_imp_remover(self):
        expected = "0.71m"
        actual = Formatter.height_imp_remover("2′4″ (0.71m)")
        self.assertEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()

        test_height_imp_remover()
        test_weight_imp_remover()
