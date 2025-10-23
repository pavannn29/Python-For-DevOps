'''
Sets in Python are an unordered collection of unique, immutable elements. They are a built-in data 
structure particularly useful for membership testing, removing duplicates, and performing mathematical 
set operations. 

# Properties of set
1. sets are unordered. 
2. sets are unindexed. 
3. there is no way to change items in sets. 
4. sets cannot contain duplicate items or values.

'''

# Creating Set

# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Creating a set from a list using the set() constructor
another_set = set([3, 4, 5, 6, 7])
print(another_set)

# Creating an empty set (note: {} creates an empty dictionary)
empty_set = set()
print(empty_set)