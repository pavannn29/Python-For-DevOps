'''
python string is a sequence of Unicode characters that is enclosed in quotation marks. In this article,
we will discuss the in-built string functions i.e. the functions provided by Python to operate on strings.

Case Changing of Python String Methods
The below Python functions are used to change the case of the strings. Let's look at some Python string methods with examples:

lower(): Converts all uppercase characters in a string into lowercase
upper(): Converts all lowercase characters in a string into uppercase
title(): Convert string to title case
swapcase(): Swap the cases of all characters in a string
capitalize(): Convert the first character of a string to uppercase

'''

# Example: Changing the case of Python String Methods

name = 'pavan gupta'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(name.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(name.lower())

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String:")
print(name.title())

# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String:")
print(name.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String:")
print(name.capitalize())

# original string never changes
print("\nOriginal String")
print(name)