#Calculate square root using given numbers
import math

c = 50
h = 30

def SquareRoot(d):
    formula = int(math.sqrt((2*c*d)/h))
    print(formula)
    
d = int(input("Give me a number to calculate square root: "))
d.__round__()

ans = SquareRoot(d)