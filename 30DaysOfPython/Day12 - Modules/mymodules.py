import random, math, statistics, string, sys
from random import randint
ascii = string.ascii_letters+string.digits
hexSys = string.ascii_letters[:6] + string.digits

def random_user_id():
    print('User ID: '+ ''.join(random.choice(ascii) for n in range(6)))
    #random(string.ascii_letters)
    #print(''.join(random.choice(ascii) for n in range(6)))
#help(random)
#print(random_user_id())

def user_id_gen_by_user():
    numChar = int(input("Enter number of characters to use: "))
    numIDs = int(input("Number of IDs to generate: "))
    totalIDs = 0
    
    while numIDs > 0:
        print('User ID:',''.join(random.choice(ascii) for n in range(numChar)))
        totalIDs+=1
        if totalIDs == numIDs:
            break
#user_id_gen_by_user()

def rgb_color_gen():
    res = 'rgb(%d,%d,%d)'%(randint(0, 255), randint(0, 255), randint(0,255))
    print(res)
#print(rgb_color_gen())

def list_of_hexa_colors():
    hexList = []
    out = '#%s'%(''.join(random.choice(hexSys) for n in range(6)))
    hexList.append(out)
    print(hexList)
#print(list_of_hexa_colors())
#print(string.ascii_letters[:6])
#print(string.digits)

def list_of_rgb_colors():
    rgbList = []
    res = 'rgb(%d,%d,%d)'%(randint(0, 255), randint(0, 255), randint(0,255))
    rgbList.append(res)
    print(rgbList)
#print(list_of_rgb_colors())

def generate_colors(colorChoice, numb):
    endHex = 0
    endRgb = 0
    hexList = []
    rgbList = []
    # hexOut = '#%s'%(''.join(random.choice(hexSys) for n in range(6)))
    # rgbOut = 'rgb(%d,%d,%d)'%(randint(0, 255), randint(0, 255), randint(0,255))

    if colorChoice == 'hexa':
        while numb > 0:
            hexOut = '#%s'%(''.join(random.choice(hexSys) for n in range(6)))
            hexList.append(hexOut)
            endHex+=1
            if endHex == numb:
                break
        print(hexList)
    if colorChoice == 'rgb':
        while numb > 0:
            rgbOut = 'rgb(%d,%d,%d)'%(randint(0, 255), randint(0, 255), randint(0,255))
            rgbList.append(rgbOut)
            endRgb+=1
            if endRgb == numb:
                break
        print(rgbList)     
# print(generate_colors('hexa',4))
# print(generate_colors('rgb',4))

def shuffle_list(x):
    shuff =  []
    for i in range(x):
        shuff.insert(randint(0,x),i)
    print(shuff)
# a = [1,2,3,4,5]
# shuffle_list(a)

def unique_array():
    unique_array = []
    uniSet = set()
    leng = len(uniSet)
    end = 7
    while leng < 7:
        
            unique_array.append(randint(0,9))
            print(unique_array)
            uniSet.update(unique_array)
            print(len(uniSet))
            if leng == 7:
                break
            else:
                unique_array.append(randint(0,9))
                uniSet.update(unique_array)
                leng+=1
        # if(unique_array[0] == unique_array.insert(0,randint(0,9))):
        #     break
    #print(unique_array)
    print(uniSet)
    
    # lenn = len(unique_array)
    ##uniSet.add(random.choice(string.digits) for n in range(7))
    # while leng < 7:
        #x = range(0,9)
        # unique_array.append(x)
        # uniSet.add(random.choice(unique_array))
    #     unique_array.insert(0,random.choice(string.digits))
    #     uniSet.update(unique_array.pop())
    #     #print(unique_array)
    #     if leng == 7 or lenn == 7:
    #         break
        
    #     elif unique_array[0] == unique_array[1]:
    #         continue
    # print(uniSet)
    # print(unique_array)
    #del uniSet
#help(list)
#print(unique_array)        
unique_array()
#print(string.digits[0])