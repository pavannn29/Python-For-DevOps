'''
While loop:

In while loop, the condition checked first. if it evaluate to true then the body of the loop is executed 
otherwise not!
if the loops is entered, the process of [condition check and execution] is continued until the condition
become false.

Note: if the condition never become false, the loop keeps getting execute.

'''

# Write a program to print 1 to 50 numbers using while loop.

i = 0

while(i<51):
    print(i)
    i += 1


# Write a program to print a list using while loop.

list = [1, "Pavan", "Sakshi", "utpal", "Kajal", True, False]

i = 0

while(i < len(list)):
    print(list[i])
    i += 1