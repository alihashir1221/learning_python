#Action Function
import os
def write_log(message):
    with open(r"C:\Users\Asus\Desktop\app.txt", "a") as file:
        file.write(message + "\n")

#validation function
def is_valid_email(email):
    return "@" in email and "." in email

#transformation function
def clean_and_split_email(email):
    #clean and split email into username and domain
    email = email.strip().lower()
    username , domain = email.split("@")
    return{
        "username = ": username,
        "domain = ": domain
    }

write_log("Application Started.")
# Recieve an email from the user
email = input("Enter your email: ")

#Validate the email
is_valid_email(email)

#If it is invalid log an error in the file
if not is_valid_email(email):
    write_log(f"{email} is invalid.")
#If it is valid, clean and structure the email
else:
    clean_email = clean_and_split_email(email)
    #Log what happened
    write_log(f"Processed email {clean_email}")
#log what ahppened
write_log("Application Ended")