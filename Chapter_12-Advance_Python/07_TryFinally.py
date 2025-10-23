# Python offer a "finally" clause which ensures execution of a piece of code inspective of exception.

def fun():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return 

    finally:
        print("Im inside a Finally statement")

fun()