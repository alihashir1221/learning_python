#*args is used to pass a variable number of arguments to a function. It allows you to pass any number of positional arguments to the function, which are then accessible as a tuple within the function.
def total(*args):
    print(sum(args))
total(1,2,3)
total(4,5,6,7)