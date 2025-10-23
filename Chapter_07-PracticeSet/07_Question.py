'''
Write a program to print this star pattern.

for n = 3

*
**
***

'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print("*"* i, end="")
    print("")