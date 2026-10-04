person = ['Maria', 29, 'Data Engineer', 'Berlin']
# name = person[0]
# age = person[1]
# job = person[2]
# country = person[3]
# print(len(name))

#The above method is time consuming and messy so we use unpacking method which is easy to use.
#Order of the variable must macth on the basis of list items to avoid confusion.
name, age, job, country = person
print(name)
print(country)
print(job)
print(age)

#Unpacking is clean easy and makes code simple and it is also easy to extend if want to age more items in the list we can add mre variables too.