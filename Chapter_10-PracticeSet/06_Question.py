'''
Can you change the self parameter inside a class to something else(say "Pavan"). try changing self to "slf" to "Pavan" and see the effects.
'''

# Example of question 5

from random import randint

class Train():

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def Book(self, Fro, To):
        print(f"Ticket is booked in train number: {pavan.trainNo} from {Fro} to {To}")

    def getStatus(pavan,):
        print(f"The train number {pavan.trainNo} is running on time succesfully!")

    def getFare(pavan, Fro, To):
        print(f"Ticket fare in train number: {pavan.trainNo} from {Fro} to {To} is {randint(250, 1299)}")


t = Train(13055)

t.Book("Ltt", "Delhi")
t.getStatus()
t.getFare("Ltt", "Delhi")


# there in no changes in output but we need to take care of code readability and code also 