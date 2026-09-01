a = (1, 45, 56443, 54, 76, "Ali","Python", 4.5, 12, True)
no = a.count(4.5) #counts the total number of occurrences of the given element in the tuple 
print(no)

#tupple.index
index = a.index(4.5) #returns the index of the first occurrence of the given element in the tuple
print(index) 

#concatenation of tuples using + operator
a = (1, 45, 56443, 54, 76, "Ali","Python", 4.5, 12, True)
b = (1, 4, 5, 6, 7, 8, 9, 10)
concatenated_tuple = a + b #here we are concatenating two tuples a and b using the + operator. The result is a new tuple that contains all the elements from both tuples in the order they were added.
print(concatenated_tuple)

b = (1, 4, 5, 6, 7, 8, 9, 10)
concatenated_tuple = b * 3 #here we are concatenating the tuple b with itself 3 times using the * operator. The result is a new tuple that contains all the elements from the original tuple repeated 3 times in the order they were added.
print(concatenated_tuple)

#numbers length using len() function
numbers = (10, 20, 30, 40)
print(len(numbers))

#to check elements in a tuple using the in operator
fruits = ("apple", "banana", "mango")
print("apple" in fruits)

