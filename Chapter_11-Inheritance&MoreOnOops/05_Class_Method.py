# A class method is method which is bound to the class and not the ovject of the class.


class Employee():
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attributes of a is {cls.a}")

e = Employee()
e.a = 45

e.show()