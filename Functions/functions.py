###FUNCTIONS####

#defining a function

def greet_user():
    print("Hello")
    
greet_user()

def greet_user(username):
    print("Hello, " + username.title() + "!")
    
greet_user("brandon")

def build_person(first_name, last_name, middle_name = ""):
    #return dictionary of info about person
    person = {"first": first_name, "last": last_name}
    if middle_name:
        person["middle"] = middle_name
    return person
musician = build_person("Kanye", "West", "Andre")
print(musician)

"""def formatted_person(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease enter your name: ")
    print("(Enter 'q' at any time to quit)")
    f_name = raw_input("First name: ")
    if f_name == 'q':
      break
    l_name = raw_input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = formatted_person(f_name, l_name)
    print("\nHello, "+ formatted_name + "!")""" 
    
## passing a list

def greet_users(names):
    for name in names:
        message = "Hello," + name.title() + "!"
        print(message)

users = ['Opal', 'Brandon', 'Carl']
greet_users(users)

## modifying list in function
unprinted = ['iphone', 'robot', 'godzilla']
completed = []

while unprinted:
    current = unprinted.pop()
    print("Printing: " + current)
    completed.append(current)
    
print("\nHave been printed: ")
for complete in completed:
    print(complete)


# separate into two funcs
def print_models(unprinted, printed):
    while unprinted:
        current = unprinted.pop()
        print("Printing: " + current)
        completed.append(current)
def display(completed):
    print("\nHave been printed: ")
    for complete in completed:
        print(complete)
        
unprinted = ['iphone', 'robot', 'godzilla']
completed = []
print_models(unprinted, completed)
display(completed)

#passing arbitrary number of args ( dont know number of args)
def make_pizza(*toppping):
    print(toppping)
make_pizza('pepperoni')
make_pizza('chicken', 'onions', 'peppers')

"""def pizza(*toppings):
    print("\nMaking your pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

pizza('pepperoni')
pizza('chicken', 'onions', 'peppers')"""

## using arbitrary keyword arguments
def build_profile(first_name, last_name, **user_info):
    #build dicitonary for user
    profile = {}
    profile['firstName'] = first_name
    profile['lastName'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_prof = build_profile('andre', 'braxton', location = 'Virginia', job = 'professor')
print(user_prof)

#importing entire module
import pizza

pizza.mk_pizza(12, 'pepperoni')
pizza.mk_pizza(16, 'chicken', 'onions', 'peppers')

#import specific functions (from module_name import func_name, function0, func1)
from pizza import mk_pizza

mk_pizza(16, 'chicken', 'onions', 'peppers')

#us "as" to give function alias
from pizza import mk_pizza as mp

mp(16, 'chicken', 'onions', 'peppers', 'bacon', 'mushrooms')

#using a to give module an  alias
import pizza as p
p.mk_pizza(10, 'extra cheese')

#import all functions in module
from pizza import *
mk_pizza(8, 'olives')






