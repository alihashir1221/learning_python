def clean_email(email):
    cl_email = email.strip().lower()
    #sara@gmail.com
    username , domain = cl_email.split("@")
    return {"username": username , "domain": domain}
print(clean_email("sara@gmail.com"))