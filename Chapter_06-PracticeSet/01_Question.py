# Write a program to find the greatest of four number entered by user.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))
number4 = int(input("Enter a number: "))

if(number1>number2 and number1>number3 and number1>number4):
    print("Greatest number is number1:", number1)

elif(number2>number1 and number2>number3 and number2>number4):
    print("Greatest number is number2:", number2)

elif(number3>number1 and number3>number2 and number3>number4):
    print("Greatest number is number3:", number3)

elif(number4>number1 and number4>number2 and number4>number3):
    print("Greatest number is number4:", number4)

else:
    print("All numbers are same.")

print("End of the program")