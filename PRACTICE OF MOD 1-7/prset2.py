'''
List + for loop
Given:
numbers = [12, 5, 8, 21, 10, 7, 16]
Use a for loop to print only the numbers greater than 10.
Expected:
12
21
16
'''
numbers = [12, 5, 8, 21, 10, 7, 16]
for number in numbers:
    if number >= 10:
        print(f"The numbers greater than 10 in the list are: {number}")