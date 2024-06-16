########################## Higher Order Functions ##########################
    # In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

    # A function can take one or more functions as parameters
    # A function can be returned as a result of another function
    # A function can be modified
    # A function can be assigned to a variable
    # In this section, we will cover:

    # 1. Handling functions as parameters
    # 2. Returning functions as return value from another functions
    # 3. Using Python closures and decorators
    #
    #
    ##### Python Closures #####
        # Python allows a nested function to access the outer scope of the enclosing function. 
        # This is is known as a Closure. Let us have a look at how closures work in Python.
        # In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. 
    #
    #
    ##### Python Decorators #####
        # A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
        # Decorators are usually called before the definition of a function you want to decorate.
    #
    #
    ##### Built-in Higher Order Functions #####
        # Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce.
        # Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.
        
        ### Python - Map Function ###
            # The map() function is a built-in function that takes a function and iterable as parameters.
        
        ### Python - Filter Function ###
            # The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). 
            # It filters the items that satisfy the filtering criteria.
        
        ### Python - Reduce Function ###
            # The reduce() function is defined in the functools module and we should import it from this module. 
            # Like map and filter it takes two parameters, a function and an iterable. 
            # However, it does not return another iterable, instead it returns a single value.

from functools import reduce
import string


print('################ Higher Order Functions ################','\n')
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Opal', 'Brandon', 'Rocky', 'Shadow']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

########### EX 1 ###########

    # for country in countries:
    #     print(country)

    # for name in names:
    #     print(name)

    # for num in numbers:
    #     print(num)
    
##### Map - change to uppercase() #####
print('##### Map - change to uppercase() ######')
def to_upper(x):
    return x.upper()

list_to_upper = map(to_upper, countries)
print(list(list_to_upper),'\n')

##### Map - Squares ######
print('##### Map - Squares ######')
def map_squares(x):
    return x**2

list_map_squares = map(map_squares, numbers)
print(list(list_map_squares),'\n')

##### Map - change to uppercase() #####
print('##### Map - change to uppercase() #####')
names_to_uppercase = map(to_upper, names)
print(list(names_to_uppercase),'\n')

##### Filter - Filter Countries with 'land' #####
print("##### Filter - Filter Countries with 'land' #####")
def filter_country_land(country):
    if 'land' in country or 'LAND' in country:
        return True  
    return False
    
filter_country = filter(filter_country_land, countries)
print(list(filter_country),'\n')

##### Filter - Filter Countries with 6 chars #####
print('##### Filter - Filter Countries with 6 chars #####')
def six_char_country(country):
    if len(country) == 6:
        return True
    return False 

sixChar = filter(six_char_country, countries)
print(list(sixChar),'\n')

##### Filter - Filter Out Starting with 'E' #####
print("##### Filter - Filter Out Starting with 'E' #####")
def starting_with_E(country):
    if country[0] == 'E':
        return True
    return False 

startE = filter(starting_with_E, countries)
print(list(startE),'\n')

##### Chain 2 or more list iterators #####
print('##### Chain 2 or more list iterators #####')
# chainFunc = map(to_upper,countries).filter(filter_country_land,countries)
# print(list(chainFunc))

##### String List type #####
print('##### Only String type in List  #####')
    # def get_string_lists(string=[]):
    #     stringonly = []
    #     print(type(string),'\n')
    #     print('__iter__' in dir(string))
    #     for line in string:
    #         if type(line) == str:
    #             stringonly.append(line)
    #     return stringonly
        
    # mixedList = ['apple,', 'orange', 'banana', 2]
    # result = map(get_string_lists,mixedList)
    # print(list(result))
    #help(string)
    # stri = 'Help'
    # if type(stri) == str:
    #     print(type(stri))

##### Reduce - sum of numbers #####
print('##### Reduce - sum of numbers #####')
def sum_numbers(x,y):
        return int(x) + int(y)
    
summ = reduce(sum_numbers,numbers)
print(summ,'\n')

##### Reduce - concat countries and format #####
print('##### Reduce - concat countries and format #####')
    # def concat_countries(*args):
    #     res = '%s are north European countries'%(args)
    #     return res
    # redCountries = reduce(concat_countries,countries)

    # print(redCountries)
    
            


