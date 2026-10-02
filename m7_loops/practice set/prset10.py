#wap to print multiplication in reverse order
n = int(input("Enter the number: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")