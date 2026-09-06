#IF ELSE STATEMENT
a = int(input("Enter your age: "))
if(a > 18):
    print("Adult")
elif(a<0):
    print("Invalid negative age entered")
elif(a==0):
    print("You are entering an invalid age")
else:
    print("Minor")
print("End of program.")