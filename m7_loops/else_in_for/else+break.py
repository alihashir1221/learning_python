#check even or not 
items = [1,23,435,567,673, 87, 9, 4]
for i in items:
    if i % 2 == 0:
        print("Even number found in the list", i)
        break
else:
    print("List is full of odd numbers")