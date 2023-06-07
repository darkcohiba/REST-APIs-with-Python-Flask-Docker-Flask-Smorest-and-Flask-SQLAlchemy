def add(x, y):
    return x + y

# turned into
add_lambda = lambda x, y: x + y
# print(add_lambda(2,2))

# to use the function in one line
# print((lambda x, y: x + y)(5,5))

# using the map function to get a doubled list
numbers = [1,2,3,4,5]
doubled = list(map(lambda x: x * 2, numbers))
# doubled will be a map object so we need to convert it into a viewable object
# print(list(doubled))
# print(doubled)