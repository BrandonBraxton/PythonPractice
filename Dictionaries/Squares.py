#Given a number, generate a dictionary of squares between 1 and given number.

num = int(input("Give a number to generate squares: "))
numDict = dict()
for i in range(1,num+1):
    numDict[i] = i*i
print(numDict)    