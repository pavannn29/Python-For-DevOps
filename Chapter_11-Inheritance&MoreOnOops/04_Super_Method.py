'''
super() function is used to call the parent class’s methods. In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class.
'''

class Employee: 
    def __init__(self, name):
        self.name = name
        print("Constructor of Employee")

class Programmer(Employee):  
    def __init__(self, name):
        super().__init__(name)
        print("Constructor of Programmer")

emp = Programmer("Pavan")
print(emp.name)