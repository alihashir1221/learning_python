import os
def write_log(message):
    with open(r"C:\Users\Asus\Desktop\app.txt", "a") as file:
        file.write(message + "\n")
        print("Written")
write_log("App Started")
write_log("user checked in")