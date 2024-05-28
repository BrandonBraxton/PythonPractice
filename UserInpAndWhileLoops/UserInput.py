#User input = data type STRING -> have to cast NUMBERS
print()

name = input("What is your name?: ")
age = int(input("What is your age?: "))
height = float(input("What is your height?(in feet): "))

print()

print("Hello," + name + "")
print("You are " + str(age) + " years old.")
print("You are " + str(height) + "ft tall.")

print()