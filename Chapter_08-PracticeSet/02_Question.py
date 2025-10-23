# Write a program using function to convert Celsius to Fehrenheit.

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in to F: "))
print(f"The conversion of F into C is: ", f_to_c(f))