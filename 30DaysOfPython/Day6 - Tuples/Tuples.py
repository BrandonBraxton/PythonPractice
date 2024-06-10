############################################### TUPLES ###############################################
    # A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

    # tuple(): to create an empty tuple
    # count(): to count the number of a specified item in a tuple
    # index(): to find the index of a specified item in a tuple
    # operator: to join two or more tuples and to create a new tuple
print('######################## TUPLES ########################')
tup = tuple()
tp = ()
print('Empty Tuple: ', tup)
print('Empty tuple: ', tp,'\n')

brothers = ('AJ', 'Akeem')
sisters = ('Gaby', 'Kamora')
siblings = brothers + sisters

print('Siblings Tuple: ', siblings)
print('Number of Siblings: ', len(siblings))
family_members = ('W', 'L') + siblings
print('Family members: ', family_members)
print('Parents (slice):', family_members[:2], 'Siblings:', family_members[2:])

print('\n##################### Ex 2 #####################')
fruits = ('apples', 'bananas', 'mangoes ')
vegatables = ('carrots', 'peppers', 'onions ')
animals = ('dogs', 'cats', 'fish')

food_stuff_tp = fruits + vegatables + animals
print ('Tuples combined: ', food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print("Tuple to List: ", food_stuff_lt)

print('apples' in food_stuff_tp)
print('apples' in food_stuff_lt)