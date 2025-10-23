'''
Instance attributes in Python are variables that are unique to each individual object (instance) created from a class. They represent the specific data or state associated with a particular instance, distinguishing it from other instances of the same class.

'''

'''
Classes: A class serves as a blueprint or a template for creating objects. It defines the attributes (data or variables) and methods (functions or behaviors) that objects of that class will possess.

'''

class Employee:
    role = "Software Developer intern"    # This is class attributes
    langauge = "Java"
    salary = '12000'

pavan = Employee()
pavan.name = "Pavan Gupta"   # This is instance attributes.
pavan.langauge = "Python"     # This is instanec attributes.
print(pavan.langauge, pavan.role, pavan.salary,)
