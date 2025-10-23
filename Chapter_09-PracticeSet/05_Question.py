# Write a program to find out the line number where python i present in log file.


with open("logFile.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python word contain in log file, Line no. {lineno}")
        break
    lineno += 1

else:
    print("No, There is no python word in log file.")