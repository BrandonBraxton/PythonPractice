###################### Regular Expressions ######################
    # A regular expression or RegEx is a special text string that helps to find patterns in data.
    # A RegEx can be used to check if some pattern exists in a different data type.
    # To use RegEx in python first we should import the RegEx module which is called re.
    
    ### Methods in re Module
        # To find a pattern we use different set of re character sets that allows to search for a match in a string.

        # re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
        # re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
        # re.findall: Returns a list containing all matches
        # re.split: Takes a string, splits it at the match points, returns a list
        # re.sub: Replaces one or many matches within a string
        #[]: A set of characters
        # [a-c] means, a or b or c
        # [a-z] means, any letter from a to z
        # [A-Z] means, any character from A to Z
        # [0-3] means, 0 or 1 or 2 or 3
        # [0-9] means any number from 0 to 9
        # [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
        # \: uses to escape special characters
        # \d means: match where the string contains digits (numbers from 0-9)
        # \D means: match where the string does not contain digits
        # . : any character except new line character(\n)
        # ^: starts with
        # r'^substring' eg r'^love', a sentence that starts with a word love
        # r'[^abc] means not a, not b, not c.
        # $: ends with
        # r'substring$' eg r'love$', sentence that ends with a word love
        # *: zero or more times
        # r'[a]*' means a optional or it can occur many times.
        # +: one or more times
        # r'[a]+' means at least once (or more)
        # ?: zero or one time
        # r'[a]?' means zero times or once
        # {3}: Exactly 3 characters
        # {3,}: At least 3 characters
        # {3,8}: 3 to 8 characters
        # |: Either or
        # r'apple|banana' means either apple or a banana
        # (): Capture and group

import re

print('###################### Regular Expressions ######################','\n')

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
    
res = [(paragraph.count(key),key) for key in paragraph.split()]
filtering = set(res)
print(list(filtering))


##### valid python variable #####
def is_valid_variable(var):
    print(var.isidentifier())

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True