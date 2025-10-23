# Write a program to accept marks of 6 students and display them in sorted manners.

studentMarks = []

s1 = int(input("Enter a student mark: "))
studentMarks.append(s1)
s2 = int(input("Enter a student mark: "))
studentMarks.append(s2)
s3 = int(input("Enter a student mark: "))
studentMarks.append(s3)
s4 = int(input("Enter a student mark: "))
studentMarks.append(s4)
s5 = int(input("Enter a student mark: "))
studentMarks.append(s5)
s6 = int(input("Enter a student mark: "))
studentMarks.append(s6)

studentMarks.sort()

print(studentMarks)