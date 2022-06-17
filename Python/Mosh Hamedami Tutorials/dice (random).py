import random


class Dice():
    def dRoll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y


dice = Dice()
print(dice.dRoll())
