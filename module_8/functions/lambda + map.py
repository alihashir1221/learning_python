prices = ['$12.50', '$65.45', '$ 98.21']
print(list(map(lambda p: float(p.replace('$', '')), prices)))