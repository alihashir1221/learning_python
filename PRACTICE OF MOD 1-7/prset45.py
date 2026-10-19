'''
Exercise 17. Merging Lists with Parity Filtering
Practice Problem: Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

Given Input:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output: [25, 35, 40, 60, 90]
'''
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []
for num in list1:               #Only odd umbers from list 1
    if num % 2 != 0:
        new_list.append(num)
for num in list2:               #Only even from list 2
    if num % 2 == 0:
        new_list.append(num)
print(new_list)