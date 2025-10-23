'''
Create a class "Pets" from class "Animals" and further create a class "Dog" from "Pets". Add a method
"Bark" to the class "dog".
'''

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):

    @staticmethod
    def Bark():
        print("Bow Bow!!")


d = Dog()
d.Bark()