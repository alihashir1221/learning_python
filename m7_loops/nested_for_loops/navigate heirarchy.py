years = [2026, 2027, 2028]
months = ['Jan', 'Feb']
dates = range(1, 29)

for y in years:
    for m in months:
        for d in dates:
            print(f"Date: {d}, Month: {m}, Year: {y}")