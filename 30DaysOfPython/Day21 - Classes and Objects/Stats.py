class Stats:
    def __init__(self):
        return self
    
    def mean(x):
        sum = 0
        for i in x:
            sum+=i
        result = sum/len(x)
        return result
    
    def median(x):
        return x[len(x)//2]
    
    def mode(x):
        uniqueList = list(set(list(x)))
        modeDICT = {}
        
        for i in uniqueList:
            getCount = x.count(i)
            modeDICT[i] = getCount
            
        max_repeat = 0
        for i in uniqueList:
            getValue = modeDICT[i]
            if getValue > max_repeat:
                max_repeat = getValue
                
        res = ''
        for i in uniqueList:
            if modeDICT[i] == max_repeat:
                res = res+str(i)+" "
                
        return res
