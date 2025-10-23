# Write a program to find whether given number is prime or not.

n = int(input("Enter a Number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("The given number is Not a prime number.")
        break

else:
    print("The given number is a Prime number.")

