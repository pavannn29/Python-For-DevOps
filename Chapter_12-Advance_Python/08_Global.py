# Global keyword is used for modifying the 

a = 45

def fun():
    global a
    a = 18
    print(a)

fun()
print(a)
