'''
We are going to write a program that generates a random number and asks the user to guess it, if the 
plyer guess is higher than the actual number, the program displays "Higher number guess", Similarly. if 
the user guess is too low, the program prints "higher number please" and when the user guesses the 
correct number, the program displays the number of guesses the player user to arrive at the number.
'''

import random

n = random.randint(1, 100)
a = -1
guesses = 1

while(a != n):
    a = int(input("Guess the Number: "))
    if(a > n):
        print("Guess the lower number please!")
        guesses += 1
    elif(a<n):
        print("Guess the higher number please!")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempt.")