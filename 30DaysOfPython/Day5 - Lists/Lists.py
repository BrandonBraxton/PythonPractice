########## LISTS ############
    # There are four collection data types in Python :

    # List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
    # Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
    # Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
    # Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
    # A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.
    
######## Creating a list #########
import math


lst = list()
emptyList=list()
#print(len(emptyList))
ls = []
emptyLS=[]
#print(len(emptyLS))

######## List with 5 items - len / first item #########
nums = [1,2,3,4,5]
print('Number list: ', nums)
print('Length of number list: ', len(nums))
print('First item in list: ', nums[0],'\n')

######## Mixed data types #########
mixed_data_types = ['Brandon', 26, 5.10, bool(),'1010 Twisted Ave']
print('List of Mixed Data Types: ', mixed_data_types,'\n')

it_companies = ['Facebook', 'Google', 'Microsoft','Apple', 'IBM', 'Oracle', 'Amazon']
print('Print list: ', it_companies)
print('Print num companies in list: ',len(it_companies))
print('Print first, mid, last: ', it_companies[0], it_companies[len(it_companies)//2],it_companies[-1], '\n')

######## Modifying List #########
it_companies[5] = 'Twitter'
print('Modifying List: ', it_companies)

######## Adding to List #########
it_companies.append('Cisco')
print('Appending to end of List: ', it_companies)
it_companies.insert(len(it_companies)//2,'Instagram')
print('Inserting at index (middle of list): ', it_companies)

######## Changing item to UPPERCASE #########
it_companies[0] = it_companies[0].upper()
print('Modifying item to UPPERCASE: ', it_companies,'\n')

######## Join list with '#; #########
print('Joining a list: ', '#; '.join(it_companies),'\n')

####### Check if item exists ########
does_exist = 'Google' in it_companies
print('Checking if item exists (Google): ', does_exist, '\n')

####### Sort list ########
IT_companies = it_companies.copy()
IT_companies.sort()
print('Sorting list (ascending): ', IT_companies)
IT_companies.sort(reverse=True)
print('Sorting list (descending): ', IT_companies,'\n')

####### Reversing list ########
ITcomp = IT_companies.copy()
ITcomp.reverse()
print('Reversing list (reverse): ', ITcomp,'\n')

####### Slice first 3 ########
sliceFirst3 = it_companies.copy()
print('Slice first 3: ', sliceFirst3[3:])

####### Slice last 3 ########
sliceLast3 = it_companies.copy()
print('Slice last 3: ', sliceLast3[:len(it_companies)-3], '\n')

####### Slice out middle item ########
sliceMiddle = it_companies.copy()
print('Print List: ', it_companies)
sliceMiddle.remove(it_companies[len(it_companies)//2])
print('Slice out middle item: ', sliceMiddle )

####### Remove first item ########
it_companies.remove(it_companies[0])
print('Remove first item: ', it_companies, '\n')

######## Remove all items ########
it_companies.clear()
print('Remove all items (clear()): ', it_companies,'\n')

######## Delete list ########
del it_companies
print('Deleted List','\n')

######## Join 2 lists ########
front_end = ['HTML', 'CSS', 'JS', 'React','Redux']
back_end = ['Node', 'Express', 'MongoDB']
print('front_end:', front_end, '|| back_end:', back_end)
new_front_end = front_end.copy()
print('Join 2 lists (+): ', front_end+back_end)
front_end.extend(back_end)
print('Join 2 lists (extend): ', front_end)
new_front_end.append(back_end)
print('Join 2 lists (append()): ', new_front_end)
full_stack = front_end + back_end
full_stack.insert(5, 'Python')
full_stack.insert(6,'SQL')
print('full_stack (insert after front_end): ', full_stack,'\n')
print('################################ Exercise 2 #################################')
################################ Exercise 2 #################################

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print('Ages:', ages)
ages.sort()
print('Ages sorted: ', ages)
print("Min. age using index[0]: ",ages[0], "|| Max age using index[-1]: ",ages[-1])
print('Min. age using min():', min(ages), 'Max age using max():', max(ages))

medianAge = (ages[len(ages)//2]+ages[len(ages)//2+1])//2
print('Median age:', medianAge)

sum = sum(ages)
avg = sum//10
range = max(ages)-min(ages)
MAXtoAVG = abs(max(ages)-avg)
AVGtoMIN = abs(avg-min(ages))

print('Average age: ',avg)

print('Range of Ages: ', range)

print('Compare Max and Min to AVG - ', "MAXtoAVG:", MAXtoAVG, "|| AVGtoMIN:",AVGtoMIN,'\n')

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
print('########################################################'*2,'\n')
print('Middle country: ', countries[len(countries)//2])
first_half = countries[:len(countries)//2]
second_half = countries[len(countries)//2:]
print('First half: ', first_half,'\n')
print('Second half: ', second_half,'\n')
print('Length first half: ', len(first_half))
print('Length second half: ', len(second_half),'\n')

['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

a,b,c,*sc =['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(a,b,c,sc)
print(a)
print(b)
print(c)
print("Scandic: ", sc)