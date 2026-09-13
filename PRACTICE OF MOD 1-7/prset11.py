'''For loop + continue
Print numbers from 1 to 20, but skip all numbers that are divisible by 3.
Expected:
1
2
4
5
7
8
...
20
'''
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)