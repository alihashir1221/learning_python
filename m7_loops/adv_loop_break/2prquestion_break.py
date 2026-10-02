'''
Write a for loop that checks numbers from 1 to 50 and prints the first number that is divisible by 7, then stops the loop.

Expected output:

7
'''
for i in range(1, 51):
    if i%7 == 0:
        print(i)
        break
    