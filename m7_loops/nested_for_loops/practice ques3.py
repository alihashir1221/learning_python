'''
3. Print a growing star pattern
Use nested for loops to print:
*
**
***
****
*****
Focus: Here, the inner loop's number of repetitions should depend on the outer loop variable.
'''
for i in range(1,6):
    for j in range(i):
        print("*", end = " ")
    print()
        