'''
Exception handling: There are so many build in exceptions which are raised in python when something goes 
wrong. 
Exception in python can be handled using a try statement . the code that handled the exception
is written in the except clause.

'''

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

