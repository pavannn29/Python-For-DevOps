# Write a program to find whether a given username contains less than 10 character or not.

username = input("Enter username: ")

if(len(username)<10):
    print("your username contain less than 10 character")

else:
    print("This username is available!")