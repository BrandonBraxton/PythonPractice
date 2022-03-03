# DICTIONARIES : collection of key-value pairs

alien_0 = {"color": "green", "points" : 5}
#accessing values
print(alien_0["color"])
print(alien_0["points"])

new_pnts = alien_0["points"]
print("You just earned " + str(new_pnts) + " points!")

alien_0["x_position"] = 0
alien_0["y_position"] = 24
print(alien_0)

#starting an empty dictionary
alien_1 = {}
alien_1["color"] = "blue"
alien_1["points"] = 10
print(alien_1)

#modifying values in a dictionary
print(alien_0["color"])
alien_0["color"] = "yellow"
print(alien_0["color"])
print(alien_0)

#if statement with Dictionaries
alien_0["speed"] = "medium"

if alien_0["speed"] == "slow":
    alien_0["x_position"] +=1
elif alien_0["speed"] == "medium":
    alien_0["x_position"] +=2
else:
    alien_0["x_position"] += 3  
print("New x_position: " + str(alien_0["x_position"]))

#removing key-value pairs
print(alien_0)
del alien_0["points"]
print(alien_0)

#dictionary of similar objects
fav_food = {"Brandon": "Chicken", "Opal": "Thai", "Rocky": "Cat Food"}
print("Rocky's favorite food is " + fav_food["Rocky"].title() + ".")

#looping through dictionary
for k, v in fav_food.items():
    print("\nKey: " + k)
    print("Value: " + v)
print("")
    
#loop through keys
for name in fav_food.keys():
    print(name.title())
print("")
    
#loop through dictionary keys in order (sorted)
for name in sorted(fav_food.keys()):
    print(name.title() + ", thank you!")
print("")

#loop through values
for food in fav_food.values():
    print(food.title())
print("")
for food in sorted(fav_food.values()):
    print(food.title())
print("")

for n, f in sorted(fav_food.items()):
    print("\nKey: " + n)
    print("Value: " + f)
print("")
    
#Nesting - List of Dictionaries
alien_0 = {"color": "green", "points" : 5}
alien_1 = {"color": 'blue', "points": 10}
alien_2 = {"color": 'red', "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print (alien)

# A list in a Dictionary
pizza = {"crust": "stuffed", "toppings": ['pepperoni', 'onion', 'peppers', 'mushrooms']}

print("You ordered a " + pizza["crust"] + "-crust pizza with the following toppings: ")
for topping in pizza["toppings"]:
    print("\t" + topping)