# Count numbers greater than 10 in a list

numbers = [5, 12, 8, 25, 17, 3, 30]

count = 0

for number in numbers:
    if number > 10:
        count += 1

print("Numbers greater than 10:", count)