import math

age = 26
height = 5.10
compNum = 1+1j

#### script to calculate area of triangle ####
    #base = int(input("Enter Base: "))
    #height = int(input("Enter Height: "))
    #print("The area of the triangle is" , str(base*height))

#### script to calculate perimeter of triangle ####
    #side_a = int(input("Enter Side A: "))
    #side_b = int(input("Enter Side B: "))
    #side_c = int(input("Enter Side C: "))
    #perimeter = side_a + side_b + side_c
    #print("The perimeter of the triangle is", str(perimeter))

## calc area and perimeter of rectangle from user input ##

    # length = int(input("Length: "))
    # width = int(input("Width: "))
    # rec_area = length * width
    # rec_perimeter = 2 * (length+width)
    # print("Area of rectangle: ", rec_area)
    # print("Perimeter of rectangle: ", rec_perimeter)

## cal are and circumference of circle from user input ##

    #userRadius = int(input("Please give a number to calculate area: "))
    #area_of_circle = math.pi * math.pow(userRadius, 2)
    #print (area_of_circle)

## calculate slope ##
    # x1, y1, x2, y2 = 2,2,6,10
    # m = (y2-y1)//(x2-x1)
    #print("Slope: ", m)
    
## string comparision ##
    # print(len("python") > len("dragon"))
    # print("a" in "python" or "py" in "dragon")
    # print("jargon" in "I hope this course is not full of jargon.")
# print(len("python"))
# print(type(len("python")))
# print(float(len("python")))
# print(type(float(len("python"))))
# print(str(len("python")))
# print(type(str(len("python"))))
# print('10' == 10)

# print(math.factorial(4))
x = 1
while x < 6:
    for x in range(1,6):
        if x == 1:
            print(x,x,x,x,x)
        else:
            print(x,math.floor(math.pow(x,0)),math.floor(math.pow(x,1)),math.floor(math.pow(x,2)), math.floor(math.pow(x,3)))
    x += 1                                                                                                                                                                                       