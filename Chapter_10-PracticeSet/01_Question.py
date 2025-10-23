# Create a class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer():
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

pavan = Programmer("Pavan Gupta", 600000, 259001)
print(pavan.name, pavan.salary, pavan.pin, pavan.company)
shubham = Programmer("Shubham Gupta", 700000, 259001)
print(shubham.name, shubham.salary, shubham.pin, shubham.company)