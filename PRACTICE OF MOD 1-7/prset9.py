'''for loop + pattern
Print this pattern:

*
**
***
****
*****

Then try changing it to:
*****
****
***
**
*

Try to understand why changing the range() changes the direction.
'''
for i in range(1,6):
     print("*"*i)
     i = i + 1
    
    
#reverse
for i in range(5,0, -1):
    print("*"*i)
    