import random

target = random.randint(1, 100)

while True:
    userchoice = int((input("Guess a number between 1 and 100: ")))
    if(userchoice == target):
        print("You guessed it!")
        break
    elif(userchoice < target):
        print("Too low!")
    else:
        print("Too high!")


print("----game over----")