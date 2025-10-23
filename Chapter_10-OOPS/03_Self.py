'''
Self parameter to the instance of the class. it is autometically passed with a function call from
an object.
'''

class Employee():
    language = "Python"
    salary = "150000"

    def getInfo(self):
        print(f"The Lanaguege is {self.language}, and The salary is {self.salary}")

    @staticmethod    # Sometimes we need a function that does not use the self-parameter. We can define a static method.
    def greet():
        print("Hello, Good Morning")

pavan = Employee()  # Here self is pavan

pavan.greet()
pavan.getInfo()
# equivalent to Employee.getInfo(pavan)

