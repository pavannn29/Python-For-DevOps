# With Statement: The best way to open and close the file autometically is the with statement.

with open("myfile.txt") as f:
    print(f.read())

# In this we dont want close the file explicitly