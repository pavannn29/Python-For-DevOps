'''
1. Opening file: we can use open() function, which requires file-path and mode as arguments:
    Syntax: file = open('filename.txt', 'mode')

filename.txt: name (or path) of the file to be opened.
mode: mode in which you want to open the file (read, write, append, etc.)

'''

# Basic Example: Opening a file

f = open("file.txt")
data = f.read()
print(data)
f.close()


'''
2. Writing file: writing to a file is done using the mode "w". This creates a new file if it doesn’t exist, or overwrites the existing file if it does. The write() method is used to add content. After writing, make sure to close the file.

'''

# Basic Example: Writing a file

st = "Hello dosto, Kaise ho?"

f = open("myfile.txt", "w")

f.write(st)

f.close()

'''
Other method to read a file:

We can also use f.readline() function to read one full line at a time.

f.readline() # Read one line from the file.

'''

# Basic Example: f.readline.()

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()