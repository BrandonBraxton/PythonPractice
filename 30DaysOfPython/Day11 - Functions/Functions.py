################################ FUNCTIONS ################################

    # Defining a Function
    # A function is a reusable block of code or programming statements designed to perform a certain task. 
    # To define or declare a function, Python provides the def keyword. 
    # The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.

##### add_two_numbers #####
print('################################ FUNCTIONS #################################','\n')
def add_two_numbers(a , b):
    add = a +b
    return add
print('Calling add_two_numbers(): ',add_two_numbers(1,2))