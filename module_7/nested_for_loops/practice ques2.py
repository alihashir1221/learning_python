'''
2. Print numbers in rows
Use nested for loops to print:
1 2 3
1 2 3
1 2 3
Focus: The inner loop should print 1, 2, 3 for every iteration of the outer loop
'''
for x in range(1,4):
    for y in range(1,4):
        print(y, end=" ")
    print()