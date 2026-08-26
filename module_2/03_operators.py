#Arithmetic Operators +, -, *, /, %, **, //

# Assignment Operators =, +=, -=, *=, /=, %=, **=, //=
a = 10 - 3
print(a)  # Output: 10
b = 5
b += 3  # Equivalent to b = b + 3
print(b)  # Output: 8
c = 10
c -= 2  # Equivalent to c = c - 2
print(c)  # Output: 8
d = 5
d *= 3  # Equivalent to d = d * 3
print(d)  # Output: 15
e = 10
e /= 2  # Equivalent to e = e / 2
print(e)  # Output: 5.0
f = 10
f %= 2  # Equivalent to f = f % 2
print(f)  # Output: 0
g = 2
g **= 3  # Equivalent to g = g ** 3
print(g)  # Output: 8
h = 10
h //= 3  # Equivalent to h = h // 3
print(h)  # Output: 3


#C omparison Operators ==, !=, >, <, >=, <=
a = 10 == 10
print(a)  # Output: False

#logical Operators and, or, not

e = True and False
print(e)
f = 5 or 10
print(f)
g = 5 and 10
print(g)

#TRUTH TABLE FOR "OR"
print("True or False is: ", True or False)
print("True or True is: ", True or True)
print("False or True is: ",False or True)
print("False or False is: ", False or False)


#TRUTH TABLE FOR "AND"
print("True and False is: ", True and False)
print("True and True is: ", True and True)
print("False and True is: ",False and True)
print("False and False is: ", False and False)

#PRINT (NOT)
print(not(True))
print(not(False))