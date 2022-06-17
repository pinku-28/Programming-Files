number = input("Numbers: ")

num_conv = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "FOUR",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output = ""
for ch in number:
    output += num_conv.get(ch, "!") + " "
print(output)
