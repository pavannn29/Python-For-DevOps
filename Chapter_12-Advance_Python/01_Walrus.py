'''
The walrus operator (:=), introduce in python 3.8, it allows you to assign values to variable as part of an
expression. This operator, named for its resemblance to the eyes and tucks of a walrus, is officially 
called the "Assignment expression".
'''

if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")