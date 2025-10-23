'''
A file contain a word "monkeys" multiple times, you need to write a program which replace this word with 
"Sakshi's" by updating the same file.
'''
word = "monkeys"

with open("Monkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "Sakshi's")

with open("Monkey.txt", "w") as f:
    f.write(contentNew)
