from src.Calculator.Addition import add
from src.Calculator.Subtraction import sub
from src.Calculator.Multiplication import multiply
from src.Calculator.Division import div
from src.Calculator.Square import square
from src.Calculator.Sqrt import sqrt

class calculator:
    result = 0

    def __init__(self):
        pass

    def Addition(self, a, b):
        self.result = add(a, b)
        return self.result

    def Subtraction(self, a, b):
        self.result = sub(a, b)
        return self.result

    def Multiplication(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def Division(self, a, b):
        self.result = div(a, b)
        return self.result

    def Square(self, a):
        self.result = square(a)
        return self.result

    def Sqrt(self, a):
        self.result = sqrt(a)
        return self.result

