# destructing variables
person = ("Sam", 42, "AI")
name, _, job = person
# using underscore as a variable name to show we want to ignore it
# print(_)

# what the fuck? Create a head to the array and a tail to the array
head, *tail = ['a', 'b', 'c', 'd', 'e']

# print(head, tail)