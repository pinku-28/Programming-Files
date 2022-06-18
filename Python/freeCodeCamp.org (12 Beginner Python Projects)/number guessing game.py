from random import randint as rt, random


def guess(x):
    random_number = rt(1, x)
    guess = 0
    tries = 0
    while guess != random_number:
        tries += 1
        guess = int(input("guess: "))
        if guess < random_number:
            print("higher")
        elif guess > random_number:
            print("lower")

    print(f"you have guessed the number {random_number}")
    print(f'total tries: {tries}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    tries = 0
    while feedback != "c":
        if low != high:
            guess = rt(low, high)
        else:
            guess = low
        tries += 1
        feedback = input(
            f'is {guess} correct? High(H), low(L), or correct(C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'gg computer guessed it {guess}')
    print(f'total tries: {tries}')


computer_guess(20)
