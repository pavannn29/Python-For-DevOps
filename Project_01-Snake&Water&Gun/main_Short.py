import random

# Mapping choices
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Computer choice
computer = random.choice([-1, 0, 1])

# User choice
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

# Result logic
if computer == you:
    print("It's a Draw!")

# Winning conditions
elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You Win!")

else:
    print("You Lose!")
