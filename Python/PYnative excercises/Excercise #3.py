# write a prgoram to accept a string from the user
# and display characters that are present at an
# even index number

# word, size

word = input("word: ")
size = len(word)

for i in range(0, size - 1, 2):
    print(f"index: {i} letter: {word[i]}")

# i 'kinda get it now
