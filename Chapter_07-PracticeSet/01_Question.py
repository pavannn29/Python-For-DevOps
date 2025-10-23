# Write a program to print multiplication table of a given number using for loop. 

number = int(input("Enter a number that you want a multi. table: "))

for i in range(1, 11):
    print(f"{number} X {i} = {number * i}")

pass # cause we want to pass this for loop and run first while loop 

# Same question with while loop

number = int(input("Enter a number that you want a multi. table: "))

i = 1

while(i<11):
    print(f"{number} X {i} = {number * i}")
    i += 1
