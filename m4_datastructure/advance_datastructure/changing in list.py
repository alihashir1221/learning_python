#HOW TO ADD

letters = [1, "3", "after", 56, 96, 12]
letters.append(7)
letters.append("x")
letters.append(25)
letters.insert(0,"h")
letters.insert(8,"eight")
print(letters)

#adding into a matix 
matrix = [
    ['a', 'b', 'c'], #Row 0
    ['d', 'e', 'f'], #Row 1
    ['g', 'h', 'i']  #Row 2
]
matrix.append(['x', 'y', 'z'])
matrix.insert(2, ['a', 'k', 'e'])
matrix[1].append('4')           # We use matrix[row number ].append/insert()
matrix[0].insert(0, 1)
print(matrix)
