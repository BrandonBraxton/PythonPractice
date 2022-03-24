###CLASSES (OOP)###

#creating a class
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is sitting now!")
    def roll_over(self):
        print(self.name.title() + " rolled over!")
    def bark(self):
        print(self.name.title() + " barked!")
    

my_dog = Dog("Rocky", 2)
print(my_dog.name.title() + " is " + str(my_dog.age) + "years old.")
my_dog.sit()
my_dog.roll_over()
my_dog.bark()