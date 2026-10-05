#We can use underscore when dont want to create a variable as it consumes memory but we have to use the same num of variables in the fucntion based on the list.
person = ['John', 'Doe', 25, 'Male']
name, _, age, _ = person
print(name)
print(age)
#We can use as many underscores.