'''
Write a program to find out whether a student has passed or failed if it require a total 40% and at least 
33% in each subject to pass. Assume 4 subjects and take marks from as an input from teh user.
'''

marks1 = int(input("Enter the marks of subject 1: "))
marks2 = int(input("Enter the marks of subject 2: "))
marks3 = int(input("Enter the marks of subject 3: "))
marks4 = int(input("Enter the marks of subject 4: "))

# check for total marks

total_marks = marks1 + marks2 + marks3 + marks4

# check for total percentage 

total_percentage = (100*(marks1 + marks2 + marks3 + marks4)/400)

if(total_percentage>=40 and total_marks>=33):
    print("Congrats, you are passed and you got:", total_percentage)

else:
    print("You failed, try next year!", total_percentage)