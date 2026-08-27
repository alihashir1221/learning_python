# #slicing to find characters using [x:y] where x is the starting index and y is the ending index. The character at the ending index is not included in the output.
name = "Narendra Modi"
namelength = name[3:6]
print(namelength)

#just to print a single character from the string, we can use [x] where x is the index of the character we want to print.
character = name[0]
print(character)

#negative slicing can also be used to find characters from the end of the string. For example, name[-1] will give us the last character of the string.
name = "Narendra Modi"
print(name[-13:-10]) #prints "Nar"
print(name[10:13]) #prints "Mod"
print(name[0:3]) #prints "Nar"