'''
Exercise 3. String Indexing and Even Slicing
Practice Problem: Display only those characters which are present at an even index number in given string.
Exercise Purpose: Understand how data is stored in memory using zero-based indexing. In most languages, the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing.
Given Input: String: "pynative"
'''
string = "pynative"
even_chars = string[::2]
for char in even_chars:
    print(char)