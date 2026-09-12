#check wether bad data is present or not

#when present
names = ['Ali', 'akshay', None, 'Altman']
for name in names:
    if name is None:
        print("Bad data found:",name)
        break
else:
    print("No bad data is found.")
    
#when not present
names = ['Ali', 'akshay', 'Altman']
for name in names:
    if name is None:
        print("Bad data found:",name)
        break
else:
    print("No bad data is found.")
