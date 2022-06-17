message = input(">")
words = message.split(' ')
emojis = {
    ":)": "🙂",
    ":D": "😄",
    ":(": "☹",
    ":|": "😐",
    ":o": "😮"
}

output = ""

for word in words:
    output += emojis.get(word, word) + " "
    print(word)

print(output)

# di ko gets pero sige
