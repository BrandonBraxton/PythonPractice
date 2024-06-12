############################################### SETS ###############################################
    # Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
    # The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements.
    # In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

#sets
it_companies = {'Facebook', 'Google', 'Microsoft','Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

################################ Exercise 1 #################################

print('################################ Exercise 1 #################################')
print('IT Companies:', it_companies, '||','Type of IT Companies:', type(it_companies), '||','Length:', len(it_companies))
print('A:',A,'||','Type of A: ',type(A), 'Length:','||', len(A))
print('B:',B,'||','Type of B: ',type(B), 'Length:', '||',len(B))
print('Age:',age,'||','Type of Age: ',type(age),'||', len(age))
print()


########## Adding 1 item to set ##########
it_companies.add('Twitter')
print('Adding Twitter to set of companies: ', it_companies, '\n')

########## Adding Multiple items to set ##########
it_companies.update({'Cisco', 'Juniper', 'Aruba'})
print('Adding multiple items to set: ', it_companies)
print('Length:', len(it_companies), '\n')

########## Remove 1 item from set ##########
it_companies.remove('Twitter')
print('Removing item from set of companies: ', it_companies)
print('Length after removing:', len(it_companies), '\n')

########## Discard 1 item from set #########
it_companies.discard('Facebook')
print('Discarding item from set of companies: ', it_companies)
print('Length after discarding:', len(it_companies), '\n')

# Difference between remove and discard: Remove - throws KeyError if item not in set || Discard - doesn't throw error (does nothing if item not in set)
print('Difference between remove and discard:')
#it_companies.remove('Facebook')
it_companies.discard('Facebook')
print('Discarding item not in list (Facebook): ', it_companies, '\n')

#################### Exercise 2 ################
print('################################ Exercise 2 #################################')

###### Joining Sets ######
C = A.union(B)
print('Joining sets (union): ', C)
D = A.update(B)
print('Joining sets (update): ', D, '\n')

###### Finding Intersetion ######
intersect = B.intersection(A)
print('Finding Intersection:', intersect)

###### Finding subset ######
sub = B.issubset(A)
sup = B.issuperset(A)
print('Finding Subset:', sub)
print('Finding SuperSet:',sup)

dis = B.isdisjoint(A)
print('Disjoint:',dis)

sym = B.symmetric_difference(A)
print('Symmetric Difference:',sym, '\n')

################################ Exercise 3 #################################
print('################################ Exercise 3 #################################')

new_ages = set(age)
print("Converting to set:",new_ages)
print('Comparing Lengths of list vs set:', '||','List Len.:', len(age), '||','Set Len.:', len(new_ages))

print()
sentence = 'I am a teacher and I love to inspire and teach people'.split()
print('Sentence:', sentence, '||','Length: ', len( sentence))
sentSet = set(sentence)
print("Converting to set:",sentSet)
print("Unique words in Sentence:", len(sentSet))
