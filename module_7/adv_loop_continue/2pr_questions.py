'''
Write a for loop that prints numbers from 1 to 10, but skips all even numbers using continue.
Expected output:
1
3
5
7
9
'''
ls = [1,2,3,4,5,6,7,8,9,10]
for l in ls:
    if l % 2 == 0:
        continue
    print(l)
