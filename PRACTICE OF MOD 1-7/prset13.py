'''
For loop + break
Given:
numbers = [12, 7, 25, 4, 19, 30, 8]
Search for the number 4. Print "Found" when you find it and then stop the loop using break.
'''
numbers = [12, 7, 25, 4, 19, 30, 8]
for number in numbers:
    if number == 4:
        print("Found")
        break