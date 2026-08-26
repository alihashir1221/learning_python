a = input("Enter first number a: ")
b = input("Enter second number b: ")
c = input("Enter your firdt name: ")
d = input("Enter your last name: ")

print("First number is: ", a)
print("Second number is: ", b)

#concatination means joining two strings together. In this case we are joining the first name and last name to form a full name.

print("The name is: ", c + " " + d) #here we are concatenating the first name and last name using the + operator.

print("Sum of a and b is: ", a + b) #here a and b are strings, so the + operator concatenates them instead of adding them as numbers.
print("Sum of a and b is: ", int(a) + int(b)) #here we convert a and b to integers before adding them.