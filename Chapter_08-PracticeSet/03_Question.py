# Write a recursive function to calculate the sum of fisrt n natural number.

def sum(n):
    if(n==0):
        return 1
    return sum(n-1) + n

print(sum(4))