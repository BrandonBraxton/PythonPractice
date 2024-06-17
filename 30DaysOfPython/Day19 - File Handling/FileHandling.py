######################## File Handling ########################
# So far we have seen different Python data types.
# We usually store our data in different file formats. 
# In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section.
# First, let us get familiar with handling files with common file format(.txt).

# File handling is an import part of programming which allows us to create, read, update and delete files. 
# In Python to handle data we use open() built-in function.

# # Syntax
    # open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
    # "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    # "w" - Write - Opens a file for writing, creates the file if it does not exist
    # "x" - Create - Creates the specified file, returns an error if the file exists
    # "t" - Text - Default value. Text mode
    # "b" - Binary - Binary mode (e.g. images)
# # Opening Files for Reading
    #*#*# The default mode of open is reading, so we do not have to specify 'r' or 'rt'.
        # f = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
    #*#*# read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.
        # f = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # txt = f.read()
        # print(txt)
        # f.close()
    #*#*# print the first 10 characters of the text file.
        # f = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # txt = f.read(10)
        # print(txt)
        # f.close()
    #*#*# readline(): read only the first line
        # f = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # line = f.readline()
        # print(line)
        # f.close()
    #*#*# readlines(): read all the text line by line and returns a list of lines
        # f  = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # lines = f.readlines()
        # print(type(lines))
        # print(lines)
        # print(''.join(lines))
        # f.close()
    #*#*# splitlines(): Another way to get all the lines as a list
        # f = open('./files/reading_file_example.txt')
        # lines = f.read().splitlines()
        # print(type(lines))
        # print(lines)
        # f.close()
    #*#*# There is a new way of opening files using with - closes the files by itself. #*#*#
        # with open('./files/reading_file_example.txt') as f:
        #     lines = f.read().splitlines()
        #     print(type(lines))
        #     print(lines)
    #*#*# Opening Files for Writing and Updating #*#*#
        # To write to an existing file, we must add a mode as parameter to the open() function:

        # "a" - append - will append to the end of the file, if the file does not it creates a new file.
        # "w" - write - will overwrite any existing content, if the file does not exist it creates.
    #*#*# Deleting Files #*#*#
        ## We have seen in previous section, how to make and remove a directory using os module.
        # import os
        # os.remove('./files/example.txt')
        
        ## If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:
        # import os
        # if os.path.exists('./files/example.txt'):
        #     os.remove('./files/example.txt')
        # else:
        #     print('The file does not exist')
    #*#*# File Types #*#*#
        # File with txt Extension
        # File with txt extension is a very common form of data and we have covered it in the previous section.

        # File with json Extension
        # JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
            #Example:
                # # dictionary
                # person_dct= {
                #     "name":"Asabeneh",
                #     "country":"Finland",
                #     "city":"Helsinki",
                #     "skills":["JavaScrip", "React","Python"]
                # }
                # # JSON: A string form a dictionary
                # person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

                # # we use three quotes and make it multiple line to make it more readable
                # person_json = '''{
                #     "name":"Asabeneh",
                #     "country":"Finland",
                #     "city":"Helsinki",
                #     "skills":["JavaScrip", "React","Python"]
                # }'''
    #*#*# Changing JSON to Dictionary #*#*#
        # LOADS() - To change a JSON to a dictionary, first we import the json module and then we use loads method.

        # import json
        # # JSON
        # person_json = '''{
        #     "name": "Asabeneh",
        #     "country": "Finland",
        #     "city": "Helsinki",
        #     "skills": ["JavaScrip", "React", "Python"]
        # }'''
        # # let's change JSON to dictionary
        # person_dct = json.loads(person_json)
        # print(type(person_dct))
        # print(person_dct)
        # print(person_dct['name'])
    #*#*# Changing Dictionary to JSON #*#*#
        # DUMPS() - To change a dictionary to a JSON we use dumps method from the json module.

        # import json
        # # python dictionary
        # person = {
        #     "name": "Asabeneh",
        #     "country": "Finland",
        #     "city": "Helsinki",
        #     "skills": ["JavaScrip", "React", "Python"]
        # }
        # # let's convert it to  json
        # person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
        # print(type(person_json))
        # print(person_json)
    #*#*# Saving as JSON File #*#*#
        # We can also save our data as a json file. Let us save it as a json file using the following steps.
        # For writing a json file, we use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.

        # import json
        # # python dictionary
        # person = {
        #     "name": "Asabeneh",
        #     "country": "Finland",
        #     "city": "Helsinki",
        #     "skills": ["JavaScrip", "React", "Python"]
        # }
        # with open('./files/json_example.json', 'w', encoding='utf-8') as f:
        #     json.dump(person, f, ensure_ascii=False, indent=4)
    #*#*# File with csv Extension #*#*#
        # CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. 
        # CSV is a very common data format in data science.

        # Example:
            # "name","country","city","skills"
            # "Asabeneh","Finland","Helsinki","JavaScript"
            # Example:

            # import csv
            # with open('./files/csv_example.csv') as f:
            #     csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
            #     line_count = 0
            #     for row in csv_reader:
            #         if line_count == 0:
            #             print(f'Column names are :{", ".join(row)}')
            #             line_count += 1
            #         else:
            #             print(
            #                 f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            #             line_count += 1
            #     print(f'Number of lines:  {line_count}')
    #*#*# File with xlsx Extension #*#*#
        # To read excel files we need to install xlrd package. We will cover this after we cover package installing using pip.

        # import xlrd
        # excel_book = xlrd.open_workbook('sample.xls)
        # print(excel_book.nsheets)
        # print(excel_book.sheet_names)
    #*#*# File with xml Extension #*#*#
        # XML is another structured data format which looks like HTML. In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute. Example:XML

        # <?xml version="1.0"?>
        # <person gender="female">
        # <name>Asabeneh</name>
        # <country>Finland</country>
        # <city>Helsinki</city>
        # <skills>
        #     <skill>JavaScrip</skill>
        #     <skill>React</skill>
        #     <skill>Python</skill>
        # </skills>
        # </person>
        # For more information on how to read an XML file check the documentation

        # import xml.etree.ElementTree as ET
        # tree = ET.parse('./files/xml_example.xml')
        # root = tree.getroot()
        # print('Root tag:', root.tag)
        # print('Attribute:', root.attrib)
        # for child in root:
        #     print('field: ', child.tag)
################################################################################################################################
print('######################## File Handling ########################','\n')

def getFileCounts(in_file):
    numLines = 0
    numWords = 0

    with open(in_file) as f:
        for line in f:
            numLines +=1
            numWords += len(line.split(' '))
    print("File Name: {0}\nNumber of lines: {1}\nNumber of words: {2}\n".format(in_file[71:],numLines, numWords))
    
getFileCounts('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/obama_speech.txt')
getFileCounts('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/michelle_obama_speech.txt')

    #*#*# Changing JSON to Dictionary #*#*#
        # LOADS() - To change a JSON to a dictionary, first we import the json module and then we use loads method.

        # 
        # # JSON
        # person_json = '''{
        #     "name": "Asabeneh",
        #     "country": "Finland",
        #     "city": "Helsinki",
        #     "skills": ["JavaScrip", "React", "Python"]
        # }'''
        # # let's change JSON to dictionary
        # person_dct = json.loads(person_json)
        # print(type(person_dct))
        # print(person_dct)
        # print(person_dct['name'])
import json

# country = json.loads('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/countries_data.json')
# print(country)

#def most_spoken_language(in_file, numLanguages):
    
with open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/countries_data.json') as inf:
    data = json.load(inf)
    print(type(inf))
    print(type(data))
    print(len(data[0]))
    print(data[0]["languages"])
    print(list(data[0].keys())[2])
    #line = json.loads(data)
    
    #cntry_dict = {line}
    # print(line)
    # print(type(line))
# inf = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/countries_data.json')
# data = json.load(inf)
# print(data)
# print(type(data))
# print(data["name"].values())
#print(dict(data[0]))
# for i in data:
#     # print(i)
#     # print(type(i))
#     print(list(i.keys())[2])
#     #print(i['languages'])
#     #print(type(i['languages']))
#     # for i['languages'] in data:
#     #     i['languages']
#     word_freq = {'languages' :i['languages'].count('languages') for i['languages'] in i}
#     # Print the resulting dictionar
    
#     print(word_freq)        
# #langCount = 0
    
    
    
    
    
    
    
    
    




    
    
    
