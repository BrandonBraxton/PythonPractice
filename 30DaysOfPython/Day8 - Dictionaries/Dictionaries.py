################# Dictionaries #################
    # A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

print('################# Dictionaries #################','\n')

####### Create empty dictionary #######
dog = dict()
print('Printing empty dictionary:',dog)
print(type(dog))

###### Adding Key/Value pairs #####

dog['name'] = 'Shadow'
dog['color'] = 'black'
dog['breed'] = 'German Shepard'
dog['legs'] = 4
dog['age'] = 3

print('Adding Key/Value pairs:',dog, '\n')
print('###############################','\n')

student = {'first_name': 'Billy', 
           'last_name': 'Bob', 
           'Gender': 'Male', 
           'Age': 26, 
           'Marital Status': 'married',
           'Skills': ['python', 'java', 'c++'],
           'Country': 'United States',
           'City': 'Richmond',
           'Address': '1234 University Drive'
}
print("Creating a student dictionary:", student)
print("Student dictionary length:", len(student),'\n')

###### Get value from dictionary #####
print("Get Student Skills:", student['Skills'], '||', "Skills data-type:", type(student['Skills']),'\n')

##### Modify value for key #####
student['Skills'].append('JS')
print("Modifying value in dictionary:", student,'\n')

###### Get dictionary keys as list#####
keylist = student.keys()
print("Get dictionary keys as list:", keylist)

###### Get dictionary values as list #####
valuelist = student.values()
print('Get dictionary values as list:', valuelist)

##### Delete 1 item from dictionary #####
student.popitem()
print('Delete 1 item from dictionary:', student,'\n')

print('Deleting Dog:',dog)
#print(dog)
del dog
print ('Dog Deleted')