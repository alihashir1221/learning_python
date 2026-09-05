#What will be the length of of the following set
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s, len(s))

#the lenght of this set is 2 as python consider 20 == 20.0 so it is a single one