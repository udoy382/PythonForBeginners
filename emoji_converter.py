message = input("> ")
words = message.split(' ')
emojis = {
    ":)":"😃",
    ":(":"😔",
    ":D":"😱"
}

# for get emojy [ window key + >. key]

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)