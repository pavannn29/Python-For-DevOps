'''
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class)
'''

class Employee():       # This called base class or parent class
    company = "ITC"

    def show(self):
        print(f"The name of Employee is {self.name} and salary of employee is {self.salary}")


class Programmer(Employee):     # This called child or derived class
    company = "ITC Infortech"
    def showLanguage(self):
        print(f"The name of Employee is {self.company} and the  employee is cofortable with {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company)
