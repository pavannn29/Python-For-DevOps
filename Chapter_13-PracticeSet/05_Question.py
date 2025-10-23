# Write a program tp find the maximum of the numbers in a list using reduce function.

from functools import reduce

l = [23, 54, 87, 93, 110, 73, 96, 39, 51]

def greater(a, b):
    if(a>b):
        return a
    else:
        return b
    
print(reduce(greater, l))
