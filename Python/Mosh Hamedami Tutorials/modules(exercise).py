import utils
from random import randint

# initialize blank list
numbers = []
# assigns random value from 1-10 four times
for i in range(4):
    numbers.append(randint(0, 10))

# prints list of random numbers
print(numbers)
# assigns callname for module
# and uses numbers (list) for data values
maximum = utils.find_max(numbers)
print(maximum)
