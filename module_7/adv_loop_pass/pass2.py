days = ['mon', 'sun', 'tue', 'thurs', 'fri', 'wed']
for day in days:
    if day in ['sat', 'sun']: #dont define list variable in if condition instead create a new one like below
        continue
    print(f"Working days are: {day}")
    
    
days = ['mon', 'sun', 'tue', 'thurs', 'fri', 'wed']
weekdays = ['sun', 'sat']  #use like this
for day in days:
    if day in weekdays:  #decleare a variable and use it in 
        continue
    print(f"Working days are: {day}")
    