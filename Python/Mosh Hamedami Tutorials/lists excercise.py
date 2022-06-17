# find the largest number in a list

from random import randint

for i in range(5):
    items = [randint(0, 100), randint(0, 100), randint(0, 100)]
    print(items)

    highest = items[0]
    for i in items:
        if i > highest:
            highest = i
    print(highest)
