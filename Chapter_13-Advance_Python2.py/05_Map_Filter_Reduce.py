from functools import reduce

# Map Example

l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter Example

def even(n):
    if(n%2 == 0):
        return True
    else:
        return False
    
onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Example

def sum(x, y):
    return x + y

print(reduce(sum, l))