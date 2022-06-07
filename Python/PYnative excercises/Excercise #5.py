# write a function to return True if the
# first and last number of a given list is same
# otherwise return False

from random import randint

numbers_x = []
x_state = True

for i in range(5):
    numbers_x.append(randint(0, 50))

if numbers_x[0] != numbers_x[4]:
    x_state = False

print(f"Given: {numbers_x}")
print(f'Same: {x_state}')
print("-" * 15)

# ain't that hard really
