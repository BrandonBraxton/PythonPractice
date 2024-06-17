###### Conditionals ######
    # By default, statements in Python script are executed sequentially from top to bottom. 
    # If the processing logic require so, the sequential flow of execution can be altered in two way:

    # 1: Conditional execution: a block of one or more statements will be executed if a certain expression is true
    # 2: Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. 
    # In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.
    
print('###### Conditionals ######','\n')

## AGE CONDITIONAL ##
# print("## AGE CONDITIONAL ##")
# age = int(input('Enter your age: '))
# ageToDrive = 18
# ageNeeded = ageToDrive - age
# response = 'You need more %d years to learn to drive.'%(ageNeeded)

# if age >= 18:
#     print('You are old enough to learn to drive.')
# else:
#     print(response)
    
print()

##### AGE Difference #####
    # my_age = 27
    # your_age = int(input('Enter your age: '))
    # ageDiff = abs(your_age - my_age)
    # sameage = 'We are the same age.'
    # olderbyYears = 'You are %d years older than me.' %(ageDiff)
    # youngerbyYears = 'You are %d years younger than me.'%(ageDiff)
    # oneYounger = 'You are %d year younger than me.'%(ageDiff)
    # oneOlder = 'You are %d year older than me.'%(ageDiff)

    # if your_age < my_age and ageDiff == 1:
    #     print(oneYounger)
    # elif your_age > my_age and ageDiff == 1:
    #     print(oneOlder)
    # elif your_age > my_age:
    #     print(olderbyYears)
    # elif your_age < my_age:
    #     print(youngerbyYears)
    # else:
    #     print(sameage)
##### Greater Than of less than #####
    # numOne = int(input('Enter number one: '))
    # numTwo = int(input('Enter number two: '))

    # oneGreater = '%d is greater than %d.'%(numOne, numTwo)
    # oneLesser = '%d is less than %d.'%(numOne, numTwo)
    # eq = '%d is equal to %d.'%(numOne, numTwo)

    # if numOne > numTwo:
    #     print(oneGreater)
    # elif numOne < numTwo:
    #     print(oneLesser)
    # else:
    #     print(eq)
    
##### Student Grades #####
    # grade = int(input('Student grade: '))
    # if grade >= 90:
    #     print('Grade:','A')
    # elif grade < 90 and grade >= 70:
    #     print('Grade:','B')
    # elif grade < 70 and grade >= 60:
    #     print('Grade:','C')
    # elif grade < 60 and grade >= 50:
    #     print('Grade:','D')
    # else:
    #     print('Grade:','F')
    
##### Finding Season #####
season = {
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August'],
        'Fall': ['September', 'October', 'November'],
        'Winter': ['December', 'January', 'February']
    }
print(list(season.keys())[0])
print(season.values())
print(season.items())
print(season.get('Summer')[0])
print('April' in season.get('Spring'))

user = input('Enter the Month: ')

if user in season.get('Spring'):
    print('Season: ','Spring')
elif user in season.get('Summer'):
    print('Season: ','Summer')
elif user in season.get('Fall'):
    print('Season: ','Fall')
else:
    print('Season: ','Winter')
#### Check fruit in list ####
    # fruits = ['banana', 'orange', 'mango', 'lemon']
    # x = input("Enter a fruit: ")
    # added = '%s has been added to the list'%(x)
    # if x in fruits:
    #     print("That fruit already exits in the list.")
    # else: 
    #     fruits.append(x)
    #     print(added)
    #     print(fruits)

# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# # check IF key in dictionary, IF so print middle value 
# if 'skills' in person.keys():
#     print('Middle value of key: ', person.get('skills')[len(person['skills'])//2])
#     # check if person has value in values for given key
#     print('Python skills?', 'Python' in person.get('skills'))
#     if len(person.get('skills')) == 2 and 'JavaScript' in person.get('skills') and 'React' in person.get('skills'):
#         print("You are a frontend developer.")
#     elif len(person.get('skills')) == 3 and 'Node' in person.get('skills') and 'Python' in person.get('skills') and 'MongoDB' in person.get('skills'):
#         print("You are a backend developer.")
#     elif len(person.get('skills')) == 3 and 'Node' in person.get('skills') and 'React' in person.get('skills') and 'MongoDB' in person.get('skills'):
#         print("You are a fullstack developer")
#     else:
#         print('Based on Skills:', 'unknown title')

# marriedFinland = '%s %s live in %s. He is married'%(person['first_name'], person['last_name'], person['country'])

# if person['is_marred' ]== True and person['country'] == 'Finland':
#     print(marriedFinland)
# else:
#     print('Not married or not living in Finland')