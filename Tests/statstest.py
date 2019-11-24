import unittest

from Csvreader.Csvreader import csvreader
from Calculator.Calculator import Calculator
from Statistics.Stats import Statistics



class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/csvfiles/TestStats.csv')

    # def setUp(self) -> None:
    # self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

if __name__ == '__main__':
    unittest.main()
