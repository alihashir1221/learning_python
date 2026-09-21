#wap to check if a number is prime or not 
num = int(input("Enter you number: "))
for i in range (2, num):
    if num % i == 0:
        print(f"{num}is not prime.")
        break
else:
    print("Number is prime")