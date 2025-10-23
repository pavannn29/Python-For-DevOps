'''
A for loop is used to iterate through a sequence like list, tuple or string. It allow to execute a block of code repeatedly, once for each item in the sequence.

'''

# Write a program to print 1 to 50 numbers using for loop.

i = 0

for i in range(0,51):
    print(i)
    i += 1

# list Iteration using for loop.

l = [12, 24, 29, 65, 74]

for i in l:
    print(i)