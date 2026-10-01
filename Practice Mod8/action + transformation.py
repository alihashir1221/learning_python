'''
Q2 — Action + Transformation
Write a function double_number(n) that:
- Takes a number.
- Doubles the number.
- Returns the transformed value.
- Example: double_number(5) → 10
'''
def double_number(number):
    doublenumber = number * 2
    print(f"The double of number {number} is: {doublenumber}")
num = int(input("Enter a number: "))
double_number(num)
