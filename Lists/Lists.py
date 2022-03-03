import re


states = ["VA", "NY", "MD", "NC", "DE"]

print(states)
print(states[0])
print(states[0].title())
print(states[-1])

message = "I live in " + states[0].title() + "!"
print(message)

states[1] = "NJ"
print(states)

#append to end
states.append("NY")
print(states)

#insert at index
states.insert(0, "GA")
print(states)

#delete index
del states[0]
print(states)

#pop index value (from end of list)
popped = states.pop()
print(states)
print(popped)
print(states.pop(0))
print(states)

#remove based off value
states.remove("DE")
print(states)

#sort
states.sort()
print(states)
#sort reverse
states.sort(reverse=True)
print(states)
#length of list
print(len(states))


#WORKING WITH LISTS

states = ["VA", "NY", "MD", "NC", "DE"]
for state in states:
    print(state)
    
#using range
numbers = list(range(0,10))
print(numbers)

#even numbers
numbers = list(range(0,10,2))
print(numbers)
#squares
square=[]
for value in range(1,11):
    square.append(value**2)
print(square)

#simple statistics
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

#slicing list
players = ["Bill", "Bob", "Charles", "David", "Eric"]
print(players[0:])
print(players[1:3])
print(players[:4])

#copying a list
my_ints = [1,2,3,4,5]
your_ints = my_ints[:]
print("my ints: " + str(my_ints))
print("your_ints: " + str(your_ints))
my_ints.append(6)
your_ints.append(7)
print("my ints: " + str(my_ints))
print("your_ints: " + str(your_ints))
