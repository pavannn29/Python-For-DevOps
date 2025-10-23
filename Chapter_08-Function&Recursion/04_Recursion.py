'''
Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem by breaking it into smaller, simpler subproblems.

In Python, recursion is especially useful for problems that can be divided into identical smaller tasks, such as mathematical calculations, tree traversals or divide-and-conquer algorithms.

A recursive function is just like any other Python function except that it calls itself in its body.

'''

# Example: Find a factorial using recursion.

def factorial(n):
    if(n==1) or (n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number that you want factorial: "))

print(f"The factorial of given number is: {factorial(n)}")