'''
Write a for loop that prints numbers from 1 to 10, but does not print 5.
Expected output:
1
2
3
4
6
7
8
9
10
'''
for i in range(1, 11):
    if i == 5:
        continue
    print(i)