import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict= {1:"Snake", -1:"Water", 0:"Gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

""" 1 for snake
    -1 for water
    0 for gun
"""
if you == computer:
    print("It's a tie")

else:
    if you == 1 and computer == -1:
        print("You win")

    elif you == 0 and computer == -1:
        print("You lose")

    elif you == -1 and computer == 1:
        print("You lose")

    elif you == 0 and computer == 1:
        print("You win")

    elif you == 1 and computer == 0:
        print("You lose")

    elif you == -1 and computer == 0:
        print("You win")
    else:
        print("Something went wrong")
