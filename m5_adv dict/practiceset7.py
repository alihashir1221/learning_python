#can we change the values of the list insdie the set?
s = {1, 2, 3, 4, 5, "Ali", [1,2]}
#this will give an error because list is mutable and set can only have immutable values.
s.update([3,4])
print(s)