class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2
    def cube(self):
        return self.number ** 3
    def square_root(self):
        return self.number ** 0.5
    @staticmethod
    def greet():
        print("Hello! ")
Calculator.greet()
calc = Calculator(9)
print(f"Square :{calc.square()}")
print(f"Cube: {calc.cube()}")
print(f"Square root: {calc.square_root()}")