p1 = "Make a lot of money"
p2 = "buy now"
p3 = "Subscirbe this"
p4 = "Click This"

message = input("Enter Your Comment :")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a SPAM!")

else:
    print("This is not a SPAM!")