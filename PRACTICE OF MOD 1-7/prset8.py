'''
Dictionary + .items() + if

Given:

students = {
    "Ali": 85,
    "Tushar": 38,
    "Adnan": 67,
    "Rahul": 42,
    "Aman": 91
}
Using .items(), print the name and marks of students who scored 60 or more.

Expected:
Ali 85
Adnan 67
Aman 91
'''
students = {
    "Ali": 85,
    "Tushar": 38,
    "Adnan": 67,
    "Rahul": 42,
    "Aman": 91
}
for key, values in students.items():
    if values >= 60:
        print(key, values)