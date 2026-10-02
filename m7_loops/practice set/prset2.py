#wap to greet all the person names with S
list = ["Harry", "Soham", "Sachin", "Rahul"]
for l in list:
    if l.startswith(tuple("S")):
        print(f"Hello {l}")