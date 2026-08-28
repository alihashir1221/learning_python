#USING len() function to find the length of a string
name=("Ali Hashir")
print(len(name))

#String.endswith() method is used to check if a string ends with a specific character or substring. It returns True if the string ends with the specified character or substring, and False otherwise.
name = "Ali Hashir"
print(name.endswith("shi"))

name = "Ali Hashir"
print(name.endswith("shir"))

name = "Ali "
print(name.endswith("li ")) #even and empty space matters

#string.count() method is used to count the number of times a character occured 
name = "ALIHASHIR"
print(name.count("I"))