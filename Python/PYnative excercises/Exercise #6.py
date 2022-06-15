# iterate the given list of numbers and
# print only those numbers which
# are divisible by 5

from random import randint

numbers = []

for i in range(5):
    n = randint(1, 100)
    numbers.append(n)

print(f'original numbers: {numbers}')
print(f'Is divisible by 5: ')

for num in numbers:
    if num % 5 == 0:
        print(num)

# kung ayaw mo gumana edi wag
# jk gumana na
