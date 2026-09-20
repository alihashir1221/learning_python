'''
1. Allow upto 3 attempts.
2. If the user types "yes", print "Glad we are on the same page."
3. Otherwise print "3 strikes, You are out!"
'''
attempt = 3
while attempt > 0:
    answer = input("Do you agree?(yes/no): ")
    if answer == "yes":
        print("Glad, we are on the same page.")
        break
    attempt -= 1
else:
    print("3 strikes you are out")
