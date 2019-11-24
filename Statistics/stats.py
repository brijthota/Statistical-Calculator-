from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Csvreader.Csvreader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result


    def median(self):
        self.result = median(self.data)
        return self.result

    def mode(self):
        self.result = mode(self.data)
        return self.result