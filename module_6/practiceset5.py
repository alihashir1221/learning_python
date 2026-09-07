#WAP TO FIND WETHER A NAME IS GIVEN IN THE LIST OR NOT 
a = ["Ali", "Adnan", "Tushar", "Rishi", "Jaggu"]
b = input("Enter a name to find in the list")
if( b in a):                                #we in function to find wether it exists in the list or not
    print("Name exists in the list")
else:
    print("Name doesn't exist in the list")