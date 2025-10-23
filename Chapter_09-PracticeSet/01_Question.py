# Write a program to read a text from given file "poems.txt" and find out whether it contain "Twinckle" word.

f = open("Poem.txt")
content = f.read()
if("Twinkle" in content):
    print("The word Twinkle is present in the content")

else:
    print("The word Twinkle is Not present in the content")

f.close()