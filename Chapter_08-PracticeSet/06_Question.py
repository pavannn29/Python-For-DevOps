# Write a python function to print multiplication table of given number.

def multiply(n):
    for  i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter the number that you want a multi. table: "))

multiply(n)

