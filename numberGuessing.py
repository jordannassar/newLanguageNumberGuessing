import random
secretNumber = random.randint(1, 10)
userInput = int(input("Guess a number between 1 and 10: "))
while userInput != secretNumber:
    if userInput > secretNumber:
        print("Too high!")
    else:
        print("Too low!")
    userInput = int(input("Guess again: "))
print("You got it!")
