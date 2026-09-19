'''
1. Print a 3×3 pattern
Use nested for loops to print:
* * *
* * *
* * *
Focus: Understand that the outer loop controls rows and the inner loop controls columns/stars.
'''
for x in range(1,4):
    for y in range(1,4):
        print("*", end=" ")
    print()