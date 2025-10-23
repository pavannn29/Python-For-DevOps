'''
In Python, a string is a sequence of characters enclosed in quotes. It can include letters, numbers, symbols 
or spaces. Since Python has no separate character type, even a single character is treated as a string with 
length one. Strings are widely used for text handling and manipulation.

'''

# Creating a string 

# String can be created using either single('...') or Double("..") qouets. Both behave the same.

s1 = 'Hello, Python learner'
s2 = "What are you doing?"

print(s1)
print(s2)

# Multi line string

s3 = '''Hello everyone, Today is 
my second day of learning Python.
After completing this i'm gonna 
complete Shell scripting for Automation.'''

print(s3)

# Accessing characters in String
'''
Strings are indexed sequences. Positive indices start at 0 from the left; 
negative indices start at -1 from the right 
'''

name = "Pavan"

nameshort = name[0:4] 
print(nameshort)

# Negative slicing 

name = "RohitSharma"
print(name[-9:-6]) # is same as print(name[3:7]) 