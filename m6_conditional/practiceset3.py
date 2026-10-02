#A spam comment is defined as a text containing following keywords "Make a lot of money",  "Buy now", "Subscribe this", "Click this" WAP to detect these spams.
a = "Make a lot of money"
b = "Buy now"
c = "Subscribe this"
d = "Click this"
message = input("Enter your comment: ")
if((a in message) or (b in message) or (c in message) or (d in message)):
    print("Spam")
else:
    print("Not Spam")