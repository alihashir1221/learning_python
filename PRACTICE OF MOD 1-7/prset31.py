#Exercise 6. Calculate the cube of all numbers from 1 to a given number
def findCube(n):
    cubes = []
    for num in range (1, n+1):
        cubes.append(num ** 3)
    return cubes
print(findCube(5))

