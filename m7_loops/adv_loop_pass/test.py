emails = [
    'alihashir1221@gmail.com',
    'ali.hashir@s.amity.edu',
    'OH OHKAY GUYS;',
    'importantthing@gmail.com'
]
for email in emails:
    if ';' in email:
        print('SQL injection detected')
        break           #here we use break because it is threat so instead of executing instead of using continue
    print(f"The email is: {email}")