'''
4. List + continue

Given:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Use a for loop and continue to print only the odd numbers.

Expected:
1
3
5
7
9
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if (number % 2== 0):
        continue
    print(number)