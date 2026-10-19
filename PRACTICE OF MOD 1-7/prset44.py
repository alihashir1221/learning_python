'''
Exercise 16. Numerical Palindrome Check
Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
Exercise Purpose: This exercise introduces the idea of “Reversing Logic.” Reversing a string is simple, but reversing an integer takes some math, like using division and modulo, or changing its type. This shows how data types can work differently.

Given Input:
Case 1: number = 121
Case 2: number = 125
'''
def convert():
    org_str = input("Enter a number: ")
    conv_str = str(org_str)
    pal_str = conv_str[::-1]
    if conv_str == pal_str:
        return True
    else:
        return False
print(convert())
