person = ['Maria', 29, 'Data Engineer','Spain']
name, *details, country = person
print(name)   
print(details)   
print(country)   

person = ['Maria', 29, 'Data Engineer','Spain']
name, *details = person
print(name)
print(details)

person = ['Maria', 29, 'Data Engineer','Spain']
*details, country = person
print(details)
print(country)

person = ['Maria', 29, 'Data Engineer','Spain']
*details, city, country = person
print(details)
print(city)
print(country)


#Only one astrick is allowed in the assignment, and it must be used to capture the remaining items in the list. The asterisk can be placed anywhere in the assignment, but it can only appear once.