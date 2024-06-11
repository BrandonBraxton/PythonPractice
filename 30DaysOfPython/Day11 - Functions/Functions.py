################################ FUNCTIONS ################################

    # Defining a Function
    # A function is a reusable block of code or programming statements designed to perform a certain task. 
    # To define or declare a function, Python provides the def keyword. 
    # The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.

import math
print('################################ FUNCTIONS #################################','\n')

##### Func - add_two_numbers #####
print('##### Func - add_two_numbers #####')
def add_two_numbers(a , b):
    add = a +b
    return add
print('Calling add_two_numbers(): ',add_two_numbers(1,2),'\n')

##### Func - Area of Circle #####
print('##### Func - Area of Circle #####')
def area_of_circle(radius,pi = 3.14):
    area = pi * math.pow(radius, 2)
    return area
print('Calling area_of_circle(): ', area_of_circle(2),'\n')

##### Func - Add all numbers (arbitrary) #####
print('##### Func - Add all numbers (arbitrary) #####')
def add_all_numbers(*nums):
    print(type(nums))
    sum = 0
    for i in nums:
        sum += i
    return sum
print('Calling add_all_numbers():', add_all_numbers(1,2,3,4,5), '\n')

##### Func - Temp. Converter #####
print('##### Func - Temp. Converter #####')
def convert_celsius_to_fahrenheit(celsius):
    fahr = (celsius * (9/5)) +32
    return fahr
print('Calling convert_celsius_to_fahrenheit(): ', convert_celsius_to_fahrenheit(100),'\n')

##### Func - Check Season #####
print('##### Func - Check Season #####')
def check_season(month):
    season = {
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August'],
        'Fall': ['September', 'October', 'November'],
        'Winter': ['December', 'January', 'February']
    }
    ##print(season.keys())
    ##print(season.values())
    ##print(season.items())
    ##print(season.get('Summer')[0])
    ##print('April' in season.get('Spring'))
    if month in season.get('Spring'):
        return 'Season: Spring'
    elif month in season.get('Summer'):
        return 'Season: Summer'
    elif month in season.get('Fall'):
        return 'Season: Fall'
    else:
        return 'Season: Winter'
print('Calling check_season():', check_season('May'))
print('Calling check_season():', check_season('January'))
print('Calling check_season():', check_season('June'))
print('Calling check_season():', check_season('November'),'\n')

##### Func - Calculate slope #####
print('##### Func - Calculate slope #####')
def calculate_slope(*axis):
    try:
        x1,y1,x2,y2 = axis
        slope = (y2-y1)/(x2-x1)
        return slope
    except ZeroDivisionError:
        return 'Cant Divide By Zero. Try Again!'
print('Calling calculate_slope():', calculate_slope(6,10,6,11))
print('Calling calculate_slope():', calculate_slope(8,10,1,5),'\n')

##### Func - Quadratic Formula #####
    # print('##### Func - Quadratic Formula #####')
    # def solve_quadratic_formula(a,b,c,x):
    #     equation = (a*math.pow(x,2)) + (b*x) + c
    #     res = 0

##### Func - Print List #####
print('##### Func - Print List #####')
def print_list(lst):
    for it in range(0,len(lst)):
        print(lst[it])
a = ['This', 'is', 'a','printed', 'list']
print('Calling print_list():')
print_list(a)
print()

##### Func - Reverse List #####
print('##### Func - Reverse List #####')
def reverse_list(x):
    newlist = []
    for i in x:
        newlist.insert(0,i)
    print(newlist)
    
b = ['A', 'B', 'C','D']
print('Calling reverse_list(): ')
reverse_list(b)
print()

##### Func - Capitalize list items #####
print('##### Func - Capitalize list items #####')
def capitalize_list_items(lt):
    newLt = []
    for item in lt:
        newLt.append(item.capitalize())
    print(newLt)
cap = ['This', 'is', 'a','printed', 'list']
print('Calling capitalize_list_items():')
capitalize_list_items(cap)
print()

##### Func - Add Item to list #####
print('##### Func - Add Item to list #####')
def add_item(item, itemList):
    itemList.append(item)
    print(itemList)
ls = ['This', 'is', 'a','printed', 'list']
numLS = [1,2,3,4,5]
print('Calling add_item():')
add_item('function', ls)
add_item(6, numLS)
add_item(numLS, ls)
print()

##### Func - Remove Item from list #####
print('##### Func - Remove Item from list #####')
def remove_item(item, itemList):
    if item in itemList:
        itemList.remove(item)
        print(itemList)
    else:
        print('Item not in list')
print('Calling remove_item():')
rmList = ['This', 'is', 'a','printed', 'list']
remove_item('a',rmList)
print()

##### Func - Sum of Numbers #####
print('##### Func - Sum of Numbers #####')
def sum_of_numbers(x):
    sum = 0
    for i in range(0,x+1):
        sum += i
    print(sum)
print('Calling sum_of_numbers():')
sum_of_numbers(5)
sum_of_numbers(10)
sum_of_numbers(100)
print()

##### Func - Sum of ODDs #####
print('##### Func - Sum of ODDs #####')
def sum_of_odds(odd):
    sum = 0
    for i in range(0,odd+1):
        if (i % 2) != 0:
            sum += i
    print(sum)
print('Calling sum_of_odds():')
sum_of_odds(25)
sum_of_odds(50)
sum_of_odds(100)
print()
    

##### Func - Sum of EVENs #####
print('##### Func - Sum of EVENs #####')
def sum_of_even(even):
    sum = 0
    for i in range(0,even+1):
        if (i % 2) == 0:
            sum += i
    print(sum)
print('Calling sum_of_even():')
sum_of_even(25)
sum_of_even(50)
sum_of_even(100)
print()

################################ Exerceise Lvl 2 ################################
print('################### Exerceise Lvl 2 ###################')

##### Func - Evens and Odds #####
print('##### Func - Evens and Odds #####')
def evens_and_odds(x):
    abs(x)
    oddCount = 0
    evenCount = 0
    for i in range(0,x+1):
        if (i % 2) == 0:
            evenCount += 1
        else:
            oddCount += 1
    print('The number of odds are', oddCount)
    print('The number of evens are', evenCount, '\n')

print('Calling evens_and_odds():')
evens_and_odds(100)
evens_and_odds(150)
print()

##### Func - Factorial #####
print('##### Func - Factorial #####')
def factorial(x):
    print(math.factorial(x))
print('Calling factorial():')
factorial(1)
factorial(2)
factorial(3)
factorial(4)
factorial(5)
print()

##### Func - Is Empty? #####
print('##### Func - Is Empty? #####')
def is_empty(x):
    try:
        if x is None or len(x) < 1 :
            print('This is empty')
        else:
            print('Not empty:', x)
    except TypeError:
        print("Can't check is_empty() for type")
a = []
b = [1]
c = 'a'
d = 5
e = True
print('Calling is_empty():')
is_empty(a)
is_empty(b)
is_empty(c)
is_empty(d)
is_empty(e)
print()
################################ Exerceise Lvl 3 ################################
print('################### Exerceise Lvl 3 ###################')

##### Func - Prime Number #####
print('###### Func - Prime Number #####')
def is_prime(a):
    pass

##### Func - Unique Items List #####
print('###### Func - Unique Items List #####')
def is_unique(a):
    return len(a) == len(set(a)) #? True : False
lstSet = ['a', 'b', 'c', 'd','a','b','c','d','e','e','f','g','h','i','j','k','l']
print("Calling is_unique():", is_unique(lstSet))
print()

##### Func - Same data type #####
print('##### Func - Same data type #####')
def same_data_type(x):
    for i in x:
        if type(i) != type(x[+1]):
            print('Not the same data type')
        else:
            print('Same data type')
sameType = ['a','b','c', 4]
print('Calling same_data_type():')
same_data_type(sameType)
