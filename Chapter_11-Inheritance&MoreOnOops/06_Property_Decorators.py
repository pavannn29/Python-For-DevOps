'''
The @property decorator in Python is a built-in feature that allows methods within a class to be accessed and managed like attributes, while still providing the benefits of encapsulation. It essentially converts a method into a read-only attribute, or a "getter," and provides a clear way to define corresponding "setter" and "deleter" methods for controlled modification and deletion. 
'''

class Employee():
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attributes of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    

e = Employee()
e.a = 45

e.name = "Pavan Gupta"
print(e.fname, e.lname)

e.show()