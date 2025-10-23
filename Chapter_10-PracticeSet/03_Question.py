'''
Create a class with a class attribute a; create a object from it and set 'a' directly using object.a = 0.
does this change the class attributes?
'''

class Object():
    a = 45

o = Object()
print(Object.a) # Print the class attribute because instance attributes is not present 
Object.a = 0 # This is instance attribute
print(Object.a) # Print the instance attribute because instance attributes is present 