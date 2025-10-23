# In multilevel inheritance, a class is derived from another derived class (like a chain).

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def show_role(self):
        print(f"{self.name} is an employee")

class Manager(Employee):  # Manager inherits from Employee
    def department(self, dept):
        print(f"{self.name} manages {dept} department")

mgr = Manager("Pavan")
mgr.show_role()
mgr.department("HR")