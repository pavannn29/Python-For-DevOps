'''
__init__ is a special method, often referred to as the initializer or constructor, within a class definition. It is automatically called when a new instance (object) of that class is created. The primary purpose of __init__ is to initialize the attributes of the newly created object.
'''

class Employee():
    language = "Python"
    salary = "150000"

    def __init__(self, name, salary, lanaguage): # Dunder method which is autometically called when object is created.
        self.name = name
        self.salary = salary
        self.language = lanaguage
        print("Im creating a object.")

    def getInfo(self):
        print(f"The Lanaguege is {self.language}, and The salary is {self.salary}")

    @staticmethod    # Sometimes we need a function that does not use the self-parameter. We can define a static method.
    def greet():
        print("Hello, Good Morning")

pavan = Employee("Pavan", 1200000, "JavaScript")  # Here self is pavan
# pavan.name = "Pavan Gupta"
print(pavan.name, pavan.salary, pavan.language)
