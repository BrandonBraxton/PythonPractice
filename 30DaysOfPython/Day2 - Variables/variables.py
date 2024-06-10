## Day 2: 30 Days of python programming ##

import math


first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
country = 'United States'
city = 'Richmond'
age = 28
year = 2024
is_married = bool()
is_true = True
is_light_on = False

personInfo = {
    'first_name': first_name,
    'last_name': last_name,
    'full_name': full_name,
    'country': country,
    'city': city,
    'age': age,
    'is_married': is_married,
}

first,last = "billy", "bob"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(first))
print(type(last))
print()
print('First name length: ', len(first_name))
print('Person Info: ', personInfo)
print("Length of name: ",len(first_name), len(last_name))

##math operations
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = math.pow(num_one, num_two)
floor_division = math.floor(num_one / num_two)

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

#Circle calculations
radius = 30
area_of_circle = math.pi * math.pow(radius, 2)
circum_of_circle = radius * 2
print (area_of_circle)

userRadius = int(input("Please give a number to calculate area: "))
area_of_circle = math.pi * math.pow(userRadius, 2)
print (area_of_circle)

##User input for person info##
first_name = input("First name: ")
last_name = input("Last name: ")
country = input("Country: ")
city = input("City: ")
age = int(input("Age: "))
#is_married = input("Ismarried (0/1): ")

print(personInfo)