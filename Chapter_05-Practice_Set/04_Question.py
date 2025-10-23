'''
Create a empty dictionary. Allow 4 friends to enter their favorite laguange as value and key
as thier names. Assume that the names are unique.
'''

dict = {}

name = input("Enter friend name: ")
lang = input("Enter favorite language: ")
dict.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter favorite language: ")
dict.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter favorite language: ")
dict.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter favorite language: ")
dict.update({name: lang})

print(dict)
