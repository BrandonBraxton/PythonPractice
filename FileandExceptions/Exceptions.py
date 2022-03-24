##EXCEPTIONS

#try catch blocks

try:
    print(5/0)

except ZeroDivisionError:
    print("You can't divide by zero!")


#using exceptions to prevent crashes

"""print("give me to numbers to divide")
print("enter 'q' to quit")

while True:
    first = input("\nFirst Number: ")
    if first == 'q':
        break
    second = input("\nSecond Number: ")
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)"""
        
##Handling FileNotFoundError

filename = 'programming.txt'
try:
    with open(filename, encoding= 'utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
#analyzing txt
else:
    words = contents.split()
    num_words = len(words)
    print(filename + " has about " + str(num_words) + " words.")
    
    
    