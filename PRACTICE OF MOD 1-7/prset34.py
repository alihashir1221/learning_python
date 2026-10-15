'''
Exercise 9. Print elements from a list present at odd index positions
Practice Problem: Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).
Exercise Purpose: This exercise teaches Index-Based Iteration. It helps you distinguish between an item’s value in a list and its position (index), which is fundamental for data filtering.
Given Input: my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected Output: [20 40 60 80 100]
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(1, len(my_list), 2):
    print(my_list[i], end=" ")