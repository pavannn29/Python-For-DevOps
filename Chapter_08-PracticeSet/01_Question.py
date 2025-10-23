# write a program using function to find the greatest of three number.

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

def greatestNum(num1, num2, num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    elif(num3>num2 and num1>num1):
        return num3

print(f"The Greatest number is: ", greatestNum(num1, num2, num3))
        