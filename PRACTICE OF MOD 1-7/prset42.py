'''
Exercise 28. Odd/Even List Splitter
Practice Problem: Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.
Given Input: numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
'''
numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
odd = []
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f"Even numbers are {even}\nOdd numbers are {odd}")
