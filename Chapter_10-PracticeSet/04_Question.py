# add a static method in question 2, to greet the user with hello.

class Calculator():

    def __init__(self, n):
        self.n = n 

    def square(self):
        print(f"The Square is {self.n*self.n}")
    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The SquareRoot is {self.n**1/2}")

    @staticmethod
    def greet():
        print("Hello, Calculator user!!")


a = Calculator(16)
a.greet()
a.square()
a.cube()
a.squareRoot()
    