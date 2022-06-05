from ast import Break
from random import randint

print("Welcome, summoner, to THE GUESSING GAME!")
print("-" * 30)
print("You have three guesses! Goodluck")

guesses = 0
mysteryNumber = randint(1, 10)
# print(mysteryNumber)

while guesses != 3:
    userGuess = int(input("Guess: "))
    guesses += 1
    if userGuess == mysteryNumber:
        print("GG, you won!")
        break
else:
    print("Sorry, you lost.")
