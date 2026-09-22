word = "donkey"

with open("replace_word.txt" , "r") as f:
    content = f.read()

New_content = content.replace(word , "#####")  

with open("replace_word.txt", "w") as f:
    f.write(New_content)