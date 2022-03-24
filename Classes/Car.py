#working with classes

class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model =  model
        self.year = year
        self.odometer = 0
    
    def get_name(self):
        long_name = str(self.year) + ' ' + (self.make) + ' ' + (self.model)
        return long_name.title()
    def read_odometer(self):
        print("The car has " + str(self.odometer) + " miles on it.")
    def update_odometer(self,mileage):
        #set reading to given value
        if mileage >= self.odometer:
            self.odometer = mileage
        else: 
            print("you can't roll backward an Odometer.")
    def increment_odometer(self, miles):
        #add given amount to odometer
        self.odometer += miles
        
"""new_car = Car('Mercedes', 'E420', 2022)
print(new_car.get_name())
new_car.update_odometer(500)
new_car.read_odometer()
new_car.increment_odometer(575)
new_car.read_odometer()"""


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery(80)
    
    def gas_tank(self):
        print("An electric car doe not have a gas tank.")
        

class Battery():
    def __init__(self,battery_size):
        self.battery_size = battery_size
    def batterySize(self):
        print("My car has a " + str(self.battery_size)+ "-kWh battery.")
    def get_range(self):
        if self.battery_size <= 70:
            range = 240
        elif self.battery_size > 70:
            range = 270
        
        msg = "This car has a range of approximately " + str(range)
        msg += " miles on a full charge."
        print(msg)
        
"""myTesla = ElectricCar('tesla', 'model x', 2020)
print(myTesla.get_name())
myTesla.battery.batterySize()
myTesla.battery.get_range()"""