# Write a program to filter a list of numbers which are divisible by 5.

def Divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [12, 244, 587, 675, 851, 345, 17620]

f = list(filter(Divisible5, a))

print(f)