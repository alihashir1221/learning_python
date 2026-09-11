'''
1. 🔤 String + for loop
Take a string from the user and count how many vowels (a, e, i, o, u) it contains.

Example:

Input: programming
Output: 3
'''
word = input("Enter a string: ")
count = 0
for vowels in word:
    if vowels in "aeiou":
        count = count + 1
print(count)
