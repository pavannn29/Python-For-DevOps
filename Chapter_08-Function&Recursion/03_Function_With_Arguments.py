'''
Function Argument: Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

# Example: 

def Greet(name):
    print({name}, " Have a Good day!")

Greet("Pavan")

Output: Pavan, Have a Good day!


Default Argument: a default argument is a parameter in a function definition that has a predefined value. If a value for that parameter is not provided when the function is called, the default value is used. If a value is provided during the function call, it overrides the default.

# Example: 

def Greet(name, ending = "Bye"):
    print(name, "Have a Good day!")
    print(ending)

Greet("Pavan")
Greet("Kajal", "See you")

Output:
Pavan Have a Good day!
Bye
Kajal Have a Good day!
See you

'''