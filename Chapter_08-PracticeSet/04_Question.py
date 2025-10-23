'''
Write a function to print first n lines o the following pattern:
****
***
**
*

for n = 4

'''

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

n = int(input("Enter the number: "))

print(pattern(n))