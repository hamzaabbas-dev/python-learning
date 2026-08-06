p1 = "make a lot of money"
p2 = "buy now"
p3 = "suscribe this"
p4 = "click on this"
message = input("Enter your comment: ")
if((p1 in message.lower())or(p2 in message.lower())or(p3 in message.lower())or(p4 in message.lower())):
    print("This comment is a spam!!! ")
else:
    print("This comment is not a spam: ")
