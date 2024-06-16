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
    ### The default mode of open is reading, so we do not have to specify 'r' or 'rt'.
        # f = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
    ### read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.
        # f = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # txt = f.read()
        # print(txt)
        # f.close()
    ### print the first 10 characters of the text file.
        # f = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # txt = f.read(10)
        # print(txt)
        # f.close()
    ### readline(): read only the first line
        # f = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # line = f.readline()
        # print(line)
        # f.close()
    ### readlines(): read all the text line by line and returns a list of lines
        # f  = open('/Users/brandon/git/PythonPractice/30DaysOfPython/Day19 - File Handling/file_handling_1.txt')
        # lines = f.readlines()
        # print(type(lines))
        # print(lines)
        # print(''.join(lines))
        # f.close()
    
    
