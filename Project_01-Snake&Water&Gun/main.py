'''
We all have played snake, water and gun game in our childhood. if you haven't, google the rules
of this game and write the python program to capable of playing this game with the user.

Snake beats Water (snake drinks it), Water beats Gun (water drowns it), and Gun beats Snake (gun shoots it). If both players choose the same option, the round is a draw.  

1 for snake, -1 for water and 0 for gun.

'''

import random 

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("its a Draw!")

else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You win!")
    elif(computer == 1 and you == -1):
        print("You loose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You loose!")
    elif(computer == 0 and you == -1):
        print("You loose!")
    else:
        print("Something wrong!!")