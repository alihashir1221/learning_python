'''
for + continue + break
Print numbers from 1 to 20, but:
Skip even numbers using continue
Stop completely when you reach 15 using break
Expected:
1
3
5
7
9
11
13
'''
for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)
    if i == 15:
        break