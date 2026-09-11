'''
1. Strings + if/else

Take a string as input from the user and check whether it contains the letter "a".

If it contains "a" → print "a is present"
Otherwise → print "a is not present"
'''
a = input("Enter a string: ")
b = a.find("a")
if ("a" in a):
    print("a is present ")
else:
    print("a is not present")