''' Create a class employee and add salary and increment properties to do.
Write a method 'SalaryAfterIncrement' method with a @property decorator with a setter which changes the 
value of increment based on the current salary.

'''

class Employee:
    salary = 12999
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100


e = Employee()
print(f"The Salary After Increment: {e.salaryAfterIncrement}")
e.salaryAfterIncrement = 15598.8
print(f"The Increment of the salary is: {e.increment}")