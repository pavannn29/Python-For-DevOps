# Write a class calculator to capable of finding square, cube and square root of number.

class Calculator():

    def __init__(self, n):
        self.n = n 

    def square(self):
        print(f"The Square is {self.n*self.n}")
    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The SquareRoot is {self.n**1/2}")

a = Calculator(16)
a.square()
a.cube()
a.squareRoot()
    