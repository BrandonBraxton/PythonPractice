cars = ["bmw", "mercedes", "audi", "honda"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
    
picked = "mercedes"

if picked != "bmw":
    print("I don't want a bmw!")
    
    