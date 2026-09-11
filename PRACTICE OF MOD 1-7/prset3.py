'''
Dictionary + for loop + if

Given:

marks = {
    "Ali": 87,
    "Tushar": 45,
    "Adnan": 72,
    "Rahul": 32
}
Use a for loop to print the names of students who scored 50 or more.
Expected:
Ali
Adnan
'''
marks = {
    "Ali": 87,
    "Tushar": 45,
    "Adnan": 72,
    "Rahul": 32
}
 
for key, value in marks.items():
    if value >= 50:
        print(key)