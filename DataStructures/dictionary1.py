def line():
    print('\n---------------\n')

#create a dictionary with integers as keys
colorInt = {1: 'Red', 2: 'Orange', 3:'Yellow'}


#create a dictionary colorString with strings as keys
colorString = {'R': 'Red', 'O': 'Orange', 'Y': 'Yellow'}

print('print colorInt')
for key, value in colorInt.items():
    print(key, 'corresponds to', value)

print('colorString')
for key, value in colorString.items():
    print(key, 'corresponds to', value)


line()
#print colorInt using .format()
print('.format')
for key, value in colorInt.items():
    print('Key {} has a value of {}'.format(key, value))


line()
#create a function printDictionary
#that takes in a dictionary as a param
#prints that dictionary
print('printDictionary')
def printDictionary(obj):
    for key, value in obj.items():
        print('{}: {}'.format(key,value))

printDictionary(colorInt)


#print a value in colorInt search by key
#print a value in colorString search by key
line()
print('Search by key')
print(colorInt[1])#red
print(colorString['O'])#orange

#print the length of both dictionaries
line()
print('length')
print(len(colorInt))
print(len(colorString))

#add five more colors to our list
line()
print('add five colors')
colorInt[4] = 'Green'
colorInt[5] = 'Blue'
colorInt[6] = 'Indigo'
colorInt[7] = 'Violet'
colorInt[8] = 'Turquoise'

printDictionary(colorInt)

#delete one key/value
del colorInt[8]

line()
print('delete one')
printDictionary(colorInt)

#BONUS
#NOT MANDATORY
#create a function that takes in two params
#search_value and dictionary
#prints whether search value exists in dictionary
def searchDictionary(dictionary, search_val):
    for key, value in dictionary.items():
        if value == search_val:
            print('Found it! {} is at key {}'.format(value, key))
            break
    else:
        print('No luck!')

searchDictionary(colorInt, 'Orange')#yes
searchDictionary(colorInt, 'Black')#no
