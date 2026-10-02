def clean_name(first_name, last_name, country= "n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "FROM", country)

#Postional Argument
clean_name("CHRistoPHER", "NOLAN", "DE")    #postional arguments

#Keyword Argument
clean_name(country = "DE", last_name = "NoLAN", first_name = "CHRistoPHER")

#Mixed Arguments
clean_name("CrISTOpher", "NoLAN", country = "DE")
#Rule: Must start with positional argument, once used a keyword argument it should continue with keyword argumennt
#TIP dont use mixed  argument as it it confusing

#Default Argument
clean_name("CHRistoPHER", "NOLAN")  #default argument will be used