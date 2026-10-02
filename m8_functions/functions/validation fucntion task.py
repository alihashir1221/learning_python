def check_email(email):
    return "@" in email and "." in email
print(check_email("saa@gmail.com"))
print(check_email("saa@gmailcom"))
print(check_email("saagmail.com"))
print(check_email("saagmailcom"))