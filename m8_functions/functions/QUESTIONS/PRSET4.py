# 5. Write a function called maximum() that takes three numbers and returns the greatest number.
def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(maximum(5,6,7))