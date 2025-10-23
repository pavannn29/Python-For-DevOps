# Write a program to check you are eligible or not for driving a car. using if elif else condition.

age = int(input("Enter your age: "))

if(age>= 18):
    print("Congrats, you are eligible for Driving a car")

elif(age<0):
    print("You are entering an invalide negative age")

elif(age==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent, you are not eligible for driving a car")

print("End of the Program")