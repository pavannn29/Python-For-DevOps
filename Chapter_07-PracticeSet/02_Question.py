# Write a program to great all the person names stored in list and which start with S.

list = ["Sakshi", "Kajal", "Sonakshi", "Abhay", "Soyam", "Pranav", "Sana"]

for name in list:
    if(name.startswith("S")):
        print(f"Hello, {name}")