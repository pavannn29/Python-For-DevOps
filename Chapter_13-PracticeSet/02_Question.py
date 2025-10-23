'''
Write a program to input name, marks and phone number of a student and format it using the format 
function like below:

"The name of the student is pavan, his marks are 72 and phone number is 79999 76666"

'''

name = input("Enter you name: ")
marks = int(input("Enter your marks: "))
phoneNo = int(input("Enter your phone number: "))

sen = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phoneNo)

print(sen)

