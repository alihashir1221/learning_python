marks = {
    "Ali": 87,
    "Tushar": 89,
    "Adnan": 90,
    "list": [1,2,3,4],
    0 : "Harry"
}

print(marks.items()) #returns a list of tuples containing key value pairs
print(marks.keys()) #returns a list of keys
marks.update({"Ali": 90}) #updates the value of the key
print(marks) #prints the updated dictionary
print(marks.values()) #returns a list of values
print(marks.get("Ali")) #returns the value of the key
print(marks["Adnan"]) #returns the value of the key if key is not found returns the default value