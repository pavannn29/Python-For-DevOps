# Example of raise exception

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to to divide number by zero.")
else:
    print(f"The Division a/b is {a/b}")