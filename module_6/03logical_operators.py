a = int(input("Enter your age: "))
if(a % 2 == 0):
    print("The number is even.")
if(a % 2 != 0):
    print("It is not even.") 
if (a > 18) and (a > 0):
    print("You are adult.")
elif (a == 0):
    print("You have entered 0 as your age.")
elif (a < 18) or (a == 18):
    print("You are still minor")
     