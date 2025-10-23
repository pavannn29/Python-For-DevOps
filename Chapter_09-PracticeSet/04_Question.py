# Write a program to mine a log file and out whether it contain word "python".

with open("logFile.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python word contain in log file")
else:
    print("No, There is no python word in log file.")