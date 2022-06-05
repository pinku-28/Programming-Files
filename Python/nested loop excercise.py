from doctest import OutputChecker


numbers = [2, 2, 2, 2, 6]

for i in numbers:
    output = ""
    for n in range(i):
        output += "L"
    print(output)

# hirap magets
