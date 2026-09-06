l = ["Hamza", "Umer", "Adeel", "Nomii"]

name = input("Enter your Name: ")
name1=name.strip().capitalize()

if(name1 in l):
    print("Your name is in the list! ")
else:
    print("Your name isn't in the list! ")
