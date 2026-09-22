words = ["donkey", "dog", "criminal"]

with open("replace_word.txt" , "r") as f:
    content = f.read()

for word in words :
    content = content.replace(word , "#" * len(word))

with open("replace_word.txt", "w") as f:
    f.write(content)