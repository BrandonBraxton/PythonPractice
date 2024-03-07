from Car import ElectricCar

new_car = ElectricCar("Toyota", "Prius", 2020)
print(new_car.get_name())
new_car.battery.batterySize()
new_car.battery.get_range()


#importing multiple classes from a module

from Car import Car, ElectricCar

my_Jeep = Car("Jeep", "Rubicon", 2021)
print(my_Jeep.get_name())

myTesla = ElectricCar("Tesla", "Model x", 2018)
print(myTesla.get_name())

#import entire module
import Car
my_Honda = Car.Car("Honda", "Accord", 2021)
print(my_Honda.get_name())
my_Hydunai = Car.ElectricCar("Hyundai", "Sonata", 2010)
print(my_Hydunai.get_name())

#import all classes from module (from m_name import*) // not recommended