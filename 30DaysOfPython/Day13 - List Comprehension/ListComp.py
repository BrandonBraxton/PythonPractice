########### List Comprehension ###########
    # List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. 
    # List comprehension is considerably faster than processing a list using the for loop.
##### Lambda Function #####
    # Lambda function is a small anonymous function without a name. It can take any number of arguments, but can only have one expression. 
    # Lambda function is similar to anonymous functions in JavaScript. 
    # We need it when we want to write an anonymous function inside another function.
    ### Creating a Lambda Function ###
        # To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression. 
        # Lambda function does not use return but it explicitly returns the expression.
print('###################### List Comprehension ######################','\n')

##### ListComp - Filter Neg. and Zero #####
print('##### ListComp - Filter Neg. and Zero #####')
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter = [fil for fil in numbers if fil%2==0 and fil>0]
print('Numbers List:',numbers,'\n\t','Filtered Neg. and Zero:', filter,'\n')

##### ListComp - Flatten list of list of lists to 1 Dimensional #####
print('##### ListComp - Flatten list of list of lists to 1 Dimensional #####')
list_of_lists = [[[1,2,3]], [[4,5,6]], [[7,8,9]]]
flattened = [num for row in list_of_lists for num in row for num in num]
print('Flattened List:',flattened,'\n')

##### ListComp - Create list of tuples #####
print('##### ListComp - Create list of tuples #####')
listTuple = [(num,) for num in range(0,10)]
print('ListTuples:', listTuple)
print()

##### ListComp - list with tuples to new list #####
print('##### ListComp - list with tuples to new list #####')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

newCountry = [list((country.upper(),country.upper()[:3]))for row in countries for country in row for country in country]
print(newCountry)
#output:[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

 


