"""message = raw_input("Tell the Parrot something to repeat: ")
print(message)

#from curses import raw


name = raw_input("Please enter your name: ")
print ("Hello, my name is " + name + "!")

height = input("How tall? ")
height = int(height)

if height >=60:
    print("you are tall")
else:
   print( "you are short")"""
#simple while
import sys
print(sys.version)

from http.client import responses

current = 0
while current < 5:
    print(current)
    current+=1
    
#letting user quit 
prompt = "Tell me something..."
prompt += "\nEnter 'quit' to end the program: "

message = ""

"""while message != "quit":
    message = raw_input(prompt)
    print(message)
    
active = True
while active:
    message = raw_input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)"""

#using break to exit loop

"""while True:
    city = raw_input(prompt)
    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")"""
        
#USING while loop with LISTS and DICTIONARIES
    #moving items from one list to another
    
unconfirmed_users = ["bob", "alex", "carl"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
print("\nThe following users have been confirmed: ")
for conf_user in confirmed_users:
    print(conf_user.title())
    
#removing specific values from list#
pets = ['dog', 'cat', 'turtle', 'fish', 'rabbit', 'hamster', 'dog', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling dictionary with user input

responses = {}
    #set flag to true
polling = True
while polling:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb? ")
    #store response in dictionary
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no" or repeat == 'n':
        polling = False
print("\n--- Poll Results ---")
for name, response in sorted(responses.items()):
    print(name + " would you like to climb " + response + ".")