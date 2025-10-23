'''
Operators in python can be overloaded using dunder function. these methods are called when a given 
operator is used on the objects.
'''

# Operators in python can be overloaded using the following methods

class Number():
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __sub__(self, num):
        return self.n - num.n
    
    def __mul__(self, num):
        return self.n * num.n
    
    def __truediv__(self, num):
        return self.n / num.n
    

n = Number(18)
m = Number(45)

print(n + m)
print(n - m)
print(n * m)
print(n / m)
    


'''
Other dunder methods in python:

    1. __str__(): Its is used to set what gets displayed upon calling str(obj)
    2. __len__(): Is is used to set what get displayed upon calling. __len__() or len(obj).

'''