'''
Exercise 18. Integer Digit Extraction and Reversal
Practice Problem: Write a program to extract each digit from an integer in the reverse order.

Exercise Purpose: This exercise explores “Mathematical Parsing.” Instead of converting a number to a string, use the modulo operator (%) and floor division (//) to isolate digits. This is common in low-level programming and algorithm challenges where type conversion is restricted.

Given Input: number = 7536

Expected Output: 6 3 5 7
'''

number = 7536
print("Given Number:", number)

while number > 0:
    # Get the last digit
    digit = number % 10
    
    # Remove the last digit from number
    number = number // 10
    
    print(digit, end=" ")