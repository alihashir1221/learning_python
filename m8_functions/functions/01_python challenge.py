'''
Keep only students name that starts with 'M'
students = [
    ['Maria', 85]
    ['Kumar', 65]
    ['Max', 95]
]
'''
students = [
    ['Maria', 85],
    ['Kumar', 65],
    ['Max', 95]
]
print(list(filter(lambda row: row[0].startswith('M'), students)))