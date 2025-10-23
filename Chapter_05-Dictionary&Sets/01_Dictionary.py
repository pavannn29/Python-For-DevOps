'''
Dictionary is a data structure that store the value in key: value pairs. Values in a dictionary can be
of any data type and can be duplicated. where as key cannot be repeated and must be immutable.

Some Properties of Dictionary:

1. Keys are case sensitive which means same name but different cases of Key will be treated distinctly.
2. Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
3. Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
4. Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.

'''

# Create a dictionary (As example storing multiple student marks in Hindi)

marks = {"Pavan" : 89, "Sakshi" : 85, "Rupali" : 76, "Kajal": 54}

print(marks)
print(type(marks))

