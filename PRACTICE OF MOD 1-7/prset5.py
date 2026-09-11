'''
5. String + for loop + break
Take a word from the user and search through it using a for loop.

Stop the loop when you find the first "e" and print:
Found e

For example, if the input is:
Hello
the loop should stop when it reaches the first e.
'''
strings = input("Enter a string: ")
for string in strings:
    if "e" in string:
        break
    print(string)