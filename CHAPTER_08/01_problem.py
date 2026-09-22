with open("1.1_Store.txt" , "r") as f:
    content = f.read()

if "twinkle" in content:
    print("Word Found! ")
else:
    print("Word Not Found! ")    