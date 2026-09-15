# Find duplicate elements in a list

numbers = [10, 20, 30, 20, 40, 10, 50]

duplicates = set()

for number in numbers:
    if numbers.count(number) > 1:
        duplicates.add(number)

print("Duplicate elements:", duplicates)