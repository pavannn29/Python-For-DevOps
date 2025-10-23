'''
Classes: A class serves as a blueprint or a template for creating objects. It defines the attributes (data or variables) and methods (functions or behaviors) that objects of that class will possess.

'''

class Employee:
    role = "Software Developer intern"    # This is class attributes
    language = "Java"
    salary = '12000'

pavan = Employee()
pavan.name = "Pavan Gupta"   # This is instance attributes.
print(pavan.name, pavan.salary, pavan.role)

shubham = Employee()
shubham.name = "Shubham Gupta"
print(shubham.name, shubham.salary, shubham.role)

# Here name is instance attributes and salary and roles are class attributes as they directly belong to the class 
