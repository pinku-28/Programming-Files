def emoji_converter(message):
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
    return output


message = input(">")
print(emoji_converter(message))

# di ko gets pero sige
# di ko parin talaga gets
