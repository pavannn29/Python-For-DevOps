'''
Python provides several built-in methods for dictionaries that allow for efficient manipulation, access, 
and transformation of dictionary data. Here's a list of some important Python dictionary methods:
'''

# Creating a dictionary 

marks = {"Pavan" : 89, "Sakshi" : 85, "Rupali" : 76, "Kajal": 54}

# 1. items(): Return the list with all dictionary keys with values (in tuples)

print(marks.items())

# 2. keys(): Returns a view object that displays a list of all the keys in the dictionary in order of insertion

print(marks.keys())

# 3. values(): Returns a view object containing all dictionary values, which can be accessed and iterated through efficiently

print(marks.values())

# 4. Update(): Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs. 
# With this method, you can include new data or merge it with existing dictionary entries

marks.update({"Pavan" : 92, "Vijay" : 87})
print(marks)

# 5. get(): Returns the value for the given key

print("Sakshi's Mark:", marks.get("Sakshi"))

# 6. clear(): Removes all items from the dictionary

print(marks.clear()) # Print None

# 7. pop(): Returns and removes the element with the given key

detail = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
detail.pop('Age')
print(detail) 
