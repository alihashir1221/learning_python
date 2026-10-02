# WAP to find the greatest of four numbers enetered by the user.
a = int(input("Enter number a: "))
b = int(input("Enter input b: "))
c = int(input("Enter input c: "))
d = int(input("Enter number d: "))
num = [a, b, c, d]
print("Greatest Number is ", max(num))
if (a >= b) and (a >= c ) and (a >= d):
    print("A is greater than B, C, D")
elif (b >= a) and (b >= c) and (b >= d):
    print("B is greater than A, C, D")
elif (c>= a) and (c >= b) and (c >= d):
    print("C is greater than A, C, D")
else:
    print("D is greater than A, B, C")
print("End of program")