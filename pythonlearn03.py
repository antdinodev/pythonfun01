#emoji converter
#convert :( to emojis

message = input(">")
words = message.split(' ') #split out the spaces
emojis = {
    ":)": "😃",
    ":(": "😢",
    "fart": "🤢",

}
#print(words)

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)



