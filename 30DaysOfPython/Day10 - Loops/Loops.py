##### Loops #####
    # Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:

    # 1. while loop
    # 2. for loop
    
print('############### LOOPS ###############','\n')
# print('For Loop: ')
    # for num in range(0,11):
    #     print(num)
    # print()

 # print('While Loop: ')
    # x = 0
    # while x < 11:
    #     print(x)
    #     x+=1
    # print()

 # print("Counting Down for-loop: ")
    # for num in range(10,-1,-1):
    #     print(num)
    # print()

# print("Counting Down while-loop: ")
    # x = 10
    # while x >=0:
    #     print(x)
    #     x -= 1
    # print()
    # print('Triangle: ')
    # for a in range(8):
    #     print('#' * a)
##Print Square using Char
    # for x in range(0,2):
    #     print('# ' * 8)
    #     for y in range(0,3):
    #         print('# '* 8)

#### Print formatted product of while loop ####
    # x,y= 0,0
    # #sty = '%d x %d = %d' % (x, y,product)
    # while x < 11 and y < 11:
    #     product = x * y
    #     sty = '%d x %d = %d' %(x, y, product)
    #     print(sty)
    #     x += 1
    #     y += 1
    
##### Iterate through a list using for loop #####
    # print(Iterate through a list using for loop:')
    # languages = ['Python', 'Numpy', 'Pandas','Django','Flask']
    # for lang in languages:
    #     print(lang)

##### Iterate 0 to 100 : ONLY EVEN NUMBERS | ONLY ODD NUMBERS #####
    # print('Iterate 0 to 100 : ONLY EVEN NUMBERS | ONLY ODD NUMBERS:')
    # print("EVEN numbers: ")
    # max = 0
    # while max <= 100:
    #     if max % 2 == 0 :
    #         print(max)
    #     max+=1
    # print()
    # print("ODD numbers: ")
    # min = 0
    # while min <= 100:
    #     if min % 2 != 0 :
    #         print(min)
    #     min+=1

######################################################################## EX 2 ########################################################################

### print sum of loop ###
    # print('SUM of for-loop:')
    # sum = 0
    # for x in range(101):
    #     sum+=x
    # else:
    #     print('The sum of all numbers from 0-100 is', sum)
    
### print sum of EVENS and ODDS for-loop ###
    # print('SUM of EVENS and ODDS for-loop:')
    # evenSum = 0
    # oddSum = 0
    # for num in range(0,101):
    #     if num % 2 == 0:
    #         evenSum += num
    #     if num % 2 != 0:
    #         oddSum += num
    # else:
    #     print('The sum of all evens is', evenSum, 'And the sum of all odds is', oddSum)
    
    
# print('Loop through list and find all countries containing 'land'')

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
land = []
for country in countries:
    if 'land' in country:
        land.append(country)
print(land)