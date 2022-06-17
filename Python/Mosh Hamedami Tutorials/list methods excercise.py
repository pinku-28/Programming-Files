# write a program to remove duplicates in a list

numbers = [1, 3, 5, 5, 4, 9, 4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# mindblown
