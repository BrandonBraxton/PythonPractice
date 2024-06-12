## Concat string ##
a = 'Thirty', 'Days', 'Of', 'Python'
b = 'Coding', 'For', 'All'
print('Thirty' + ' Days'+ ' Of'+ ' Python', '\n')
print("Using Join to concat string: ", ' '.join(b), '\n')

company = "Coding For All"
# print(company)
# print(len(company))

############ print UPPERCASE #################
print("Uppercase: ", company.upper(), '\n')

############ print LOWERCASE #################
print("Lowercase: ", company.lower(), '\n')

############ print CAPATILIZE #################
print("Capitalize: ", company.capitalize(), '\n')

############ print TITLE #################
print("Title: ", company.title(), '\n')

############ print SWAPCASE ###############
print("Swapcase: ", company.swapcase(), '\n')

############ slice out the first word ###############
print("Slice out the first word: ", company.strip('Coding').lstrip(), '\n')

############ use find, index methods #############
print("Check string contains (Coding): ", "Index ('C'): ",company.index('C'), "Find('o'): ", company.find('o'), "rFind('d'): ", company.rfind('d'), '\n')

############ use replace ##############
print("Use replace: ", company.replace('Coding','Python'), '\n')

############ use split ##############
print("Use split: ", company.split(' '),"FaceBook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','),'\n')

############ print character at index ##############
print("Character at index (0): ", company[0],"Character at index (10): ", company[10],'\n')

############ last index #############
print("Last index: ", company.rindex('l'),'\n')

############ Find Substring Startswith ##############
sub = "Coding"
print("Starts with Substring('Coding'): ", company.startswith(sub),'\n')

############ Ends with #############
sub = 'coding'
sub1 = "All"
print("Ends with Substring('coding'): ",company.endswith(sub),'\n')
print("Ends with Substring('coding'): ",company.endswith(sub1),'\n')

############ Remove spaces #############
str = '   Coding For All   '
print("Remove Spaces: ", str +'|', str.strip()+'|','\n')

############ isIdentifier #############
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier(), '\n')

############ Join list ##############
pyLib = ['Django', 'Flask','Bottle','Pyramid','Falcon']
print('# '.join(pyLib))

############ Tab Escape Sequence #############
chal = 'Name\tAge\tCountry\tCity'
chall = 'Asabeneh\t250\t\tFinland\tHelsinki'
print(chal.expandtabs(10))
print(chall.expandtabs(5), '\n')

########### String Formatting Method ############
radius= 10
area= 3.14 * radius**2
result='The area of a circle with a radius %d is %.2f meters'%(radius,area)
print("String Formatting Method using '%d' and '%.2f': ",result,'\n')


