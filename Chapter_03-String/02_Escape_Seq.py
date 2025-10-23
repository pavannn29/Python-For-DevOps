'''
In Python, escape characters are used when we need to include special characters in a string that are 
otherwise hard (or illegal) to type directly. These are preceded by a backslash (\), which tells Python 
that the next character is going to be a special character. They’re especially helpful for:

Formatting strings (adding tabs, newlines)
Including quotes inside quotes
Writing file paths
Inserting control characters

'''

# Detailed explanation with example

# 1. \n (Newline): Breack the string into new line

print("Hello World,\nWelcome to chapter 3 string")

# 2. \t (Tab): The \t escape character inserts a tab space between words or characters.

print("Name\tAge\tLocation")

# 3. \\ (Backslash): The \\ escape character inserts a literal backslash in the string.

print("This is backslash: \\")

# 4. \' (Single Quote): The \' escape character allows you to insert a single quote within a string that is enclosed by single quotes.

print('It\'a great day!')

# 5. \" (Double Quote): The \" escape character allows you to insert a double quote within a string that is enclosed by double quotes.

print("She said, \"Fuck you\"")

# 6. \r (Carriage Return): The \r escape character moves the cursor to the beginning of the line. It can overwrite the existing text.

print("Hello Sakshi!\rHello kajal")

