#Compute the factorial of a given number. Printed in comma-separated sequence.

def factorial(x):
    #x = int(input("Give a number to calculate the factorial: "))
    if x == 0:
        return 1
    else:
        return (x * factorial(x-1))
        
x = int(input("Give a number to calculate the factorial: "))
print(factorial(x))
#factorial(0)
#factorial(1)
#factorial(2)