prices = [120, 300, 150, 85, 90, 100]
print(list(filter(lambda p: p >= 100, prices)))

students = [
    ['Maria' , 85],
    ['Akash', 95],
    ['Shashank', 60]
]
print(list(filter(lambda row: row[1] > 70, students)))