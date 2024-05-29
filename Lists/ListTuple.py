#Given a sequence of comma-separated numbers, generate a list and a tuple

values = input("Give a list of nubmers: ")
l = values.split(",")
t = tuple(l)
print(l)
print(t)