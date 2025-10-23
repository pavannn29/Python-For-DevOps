'''
Union: The union of two or more sets creates a new set containing all unique elements from all the involved 
sets. Duplicates are automatically removed in the resulting union set.

Intersection: The intersection of two or more sets creates a new set containing only the elements that are 
common to all the involved sets.

'''

# Creating a sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union

union_set = set1.union(set2)
print("Sets after union: ",union_set)

# intersection
  
intersection_set = set1.intersection(set2)
print("Sets after intersection: ",intersection_set)