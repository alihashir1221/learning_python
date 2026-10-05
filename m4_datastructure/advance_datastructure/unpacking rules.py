#Number of variables should be equal to the number of elements in the list or tuple. Otherwise, it will throw an error.
number = [1, 2, 3, 4, 5]
first, second, third, fouth, fifth = number

#Asterisle (*) can be used to unpack the remaining elements of a list or tuple into a new list as it is used to stores leftover elements in a list or tuple.
num = [1]
num1, *rest = num
print(rest)  # Output: []

#You can unpack any sequence (list, tuple, string) into variables. 
# Anything which is iterable can be unpacked into variables. The number of variables should be equal to the number of elements in the sequence. Otherwise, it will throw an error.
# The number of variables should be equal to the number of elements in the sequence.
text = 'Hi'
first, *all = text
print(first)  # Output: H
print(all)  # Output: i