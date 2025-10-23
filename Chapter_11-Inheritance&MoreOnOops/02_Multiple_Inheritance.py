# Multiple inheritance occurs when the child class inherits from more than one parent classes.


class Employee():       # This called base class or parent class
    company = "ITC"
    name = "Default name"
    salary = "120000"
    def show(self):
        print(f"The name of Employee is {self.name} and salary of employee is {self.salary}")

class Codder():         # This is anaother parent class
    language = "Python"
    
    def printLanguage(self):
        print(f"Out of all languages here is your language: {self.language}")


class Programmer(Employee, Codder):     # This called child or derived class
    company = "ITC Infortech"

    def showLanguage(self):
        print(f"The name of company is {self.company} and the  employee is comfortable with {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()

