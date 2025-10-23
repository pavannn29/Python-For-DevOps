'''
Type casting is method to convert the python variable data.type into a certain data type order to perform the 
required operation by user. there are two types of Type conversion 1st is Implicit and 2nd is Explicit
'''

'''
implicit type Casting: In thid method, python convert the data type into another datatype autometically. 
Users dont have to involve in this process.
'''

# a to int 
a = 7
print(type(a)) 


# b to float 
b = 3.0
print(type(b)) 


# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))


# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

'''
Explicit type casting: In this method python needs user involvement to convert the variable data type into 
the required data type. 

Examples of Type Casting in Python: 

Mainly type casting can be done with these data type functions:

Int(): Python Int() function take float or string as an argument and returns int type object.
float(): Python float() function take int or string as an argument and return float type object.
str(): Python str() function takes float or int as an argument and returns string type object.
'''

# Python convert int to float 

a = 5

#typecast to float 
n = float(a)

print(n)
print(type(n))

