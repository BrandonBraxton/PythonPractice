#Define a class with 2 methods: getString from input and printString in uppercase

class StringMethods(object):
    def __init__(self):
        self.s = ""
        
    def getString(self):
        self.s = input("Give me a string: ")
    def printString(self):
        print(self.s.upper())
        
myObj = StringMethods()

myObj.getString()
myObj.printString()