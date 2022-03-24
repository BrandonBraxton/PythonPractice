file_name = '/Users/brandon/git/PythonPractice/FileandExceptions/pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
    #contents = file_object.read()
print()
#make list of lines from file

with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
    
print()
    
#working with file contents

with open(file_name) as file_object:
    lines = file_object.readlines()
    
pi_str = ''
for line in lines:
    pi_str += line.strip()
    
"""birthday = input("Enter your birthday, in form mmddyy: ")
if birthday in pi_str:
    print ("your birthday is in pi!")
else: 
    print("your birthday is not in pi")"""
##print(pi_str)
##print(len(pi_str))

## WRITING TO AN EMPTY FILE

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love programming too!\n")

##appending to a file
with open(filename, 'a') as file_object:
    file_object.write("I also love programming!\n")
    file_object.write("I love programming as well!\n")