'''
Write a class train which has methods to book a ticket, get status(no. of seats) and get the fare 
information of train running under indian railways.
'''

from random import randint

class Train():

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def Book(self, Fro, To):
        print(f"Ticket is booked in train number: {self.trainNo} from {Fro} to {To}")

    def getStatus(self,):
        print(f"The train number {self.trainNo} is running on time succesfully!")

    def getFare(self, Fro, To):
        print(f"Ticket fare in train number: {self.trainNo} from {Fro} to {To} is {randint(250, 1299)}")


t = Train(13055)

t.Book("Ltt", "Delhi")
t.getStatus()
t.getFare("Ltt", "Delhi")