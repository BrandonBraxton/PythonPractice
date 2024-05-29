#Find all numbers divisible by 7, but not a multiple of 5 - between 2000 and 3200. 
#Numbers printed - comma separated

divSeven = []

for i in range(2000,2200):
    if (i % 7) == 0 and not (i % 5) == 0:
        divSeven.append(str(i))
#print(divSeven)
print(','.join(divSeven))