s = {1, 2, 3, 35, 89, 12, 67, 22, "Ali"}
# .add() to add an element in the set 
s.add(100)
print(s)

# .remove() used to remove an element from the set
s.remove(35)
print(s)

# .discard() is used to remove an element safely without getting an error message if no elemnt is found
s.discard(11)
print(s)

# SETNAME.union(NEW SET NAME) is used to combine two different sets
a = {1, 2, 3, 4, 5}
b = s.union(a)
print(b)

# SETNAME.difference(NEW SETNAME) is used to subtract two sets
d = s.difference(a)
print(d)

#SETNAME.symmetric_difference
c = s.symmetric_difference(a)
print(c)

#SETNAME.issubest() is used to check wether it is subset of another or not
j = {9,6}
t = {1 ,89, 12}
print(t.issubset(s))

#SETNAME.issuperset() is used to check wether it is a superset or not
print(s.issuperset(t))

#SETNAME.isdisjoint() is used to check wehter it is a disjont of another set or not 
print(s.isdisjoint(j))