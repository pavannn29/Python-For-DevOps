# Write a python function which convert inch to cms.

def inch_to_cm(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The value in cms is {inch_to_cm(n)}")