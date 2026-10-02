#WAP to fill in a letter template given below with name and date. Dear <|name|>, You are selected! Your joining date is <|date|>.
date = input("Enter your joining date: ")
name = input("Enter your name: ")
letter = f"Dear {name}, \nYou are selected! \n{date}"
print(letter)

#or
#most efficient way

name = '''Dear <|name|>,
You are selected!
<|date|>'''
print(name.replace("<|name|>", "Ali Hashir").replace("<|date|>", "06/10/2004"))