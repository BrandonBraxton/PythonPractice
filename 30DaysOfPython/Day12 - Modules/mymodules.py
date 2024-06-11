import random, math, statistics, string, sys
from random import randint
ascii = string.ascii_letters+string.digits
hexSys = string.ascii_letters[:6] + string.digits

def random_user_id():
    return 'User ID: '+ ''.join(random.choice(ascii) for n in range(6))
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
    return res
#print(rgb_color_gen())

def list_of_hexa_colors():
    hexList = []
    out = '#%s'%(''.join(random.choice(hexSys) for n in range(6)))
    hexList.append(out)
    return hexList
#print(list_of_hexa_colors())
#print(string.ascii_letters[:6])
#print(string.digits)

def list_of_rgb_colors():
    rgbList = []
    res = 'rgb(%d,%d,%d)'%(randint(0, 255), randint(0, 255), randint(0,255))
    rgbList.append(res)
    return rgbList
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
        return hexList
    if colorChoice == 'rgb':
        while numb > 0:
            rgbOut = 'rgb(%d,%d,%d)'%(randint(0, 255), randint(0, 255), randint(0,255))
            rgbList.append(rgbOut)
            endRgb+=1
            if endRgb == numb:
                break
        return rgbList
            
print(generate_colors('hexa',3))
print(generate_colors('rgb',2))
        
