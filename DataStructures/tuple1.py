def line():
    print('------------\n')

def printObj(obj):
    for i in obj:
        print(i, end=' ')
    print('')

numTuple = (5, 6, 7, 8)
nameTuple = ('Bobby', 'Mike', 'Sue', 'Maggie', 'anthony')
print('Tuples:')
printObj(numTuple)
printObj(nameTuple)

#create lists of numbers and names
line()
numList = [55, 66, 77, 88]
nameList = ['Robert', 'Michael', 'Susan', 'Margaret']
print('Lists:')
printObj(numList)
printObj(nameList)

#print 2 statments identifying indexes of objects
line()
print("Indexes of items:")
print(numTuple.index(5))
print(nameTuple.index('Sue'))

#print 2 statements identifying objects at an index
# numTuple = (5, 6, 7, 8)
# nameTuple = ('Bobby', 'Mike', 'Sue', 'Maggie')
line()
print("Objects at an index:")
print(numTuple[2])
print(nameTuple[1])

#create a statement that checks if numTuple includes 30
line()
print("If an object includes an item:")
print(30 in numTuple)
print('Mike' in nameTuple)


line()
def itemFinder(item, obj):
    if(item in obj):
        print('Yes! we found', item)
    else:
        print('No, the item was not found')

    #5 in numTuple returns true

itemFinder(5, numTuple) #yes

# print all of your tuples in reverse
numTupleReverse = reversed(numTuple)
nameTupleReverse = reversed(nameTuple)
line()
print("Reversed Tuples:")
printObj(numTupleReverse)
printObj(nameTupleReverse)

#print all of your tuples sorted
numTupleSorted = sorted(numTuple)
nameTupleSorted = sorted(nameTuple)

line()
print("Sorted Tuples")
printObj(numTupleSorted)
printObj(nameTupleSorted)


#create a tuple 'myFavsTuple'
#with your favorite sports team members, tv show cast, movie cast etc
#Creates a line
line()
#creating a tuple
myFavsTuple = ('don cheadle', 'zcar','Oprah', 'Denzel', 'Sting', 'Drake')
#using a function to print a tuple
printObj(myFavsTuple)
#reversing myFavsTuple
myFavsTupleReversed = reversed(myFavsTuple)
#printing
printObj(myFavsTupleReversed)
#sorting myFavsTuple
myFavsTupleSorted = sorted(myFavsTuple)
#printing again
printObj(myFavsTupleSorted)


#bonus
#turn the above 'myFavsTuple' into a list using a function
newList = []
def tupleToList(tuple, list):
    for i in tuple:
        list.append(i)

line()
print("New List")
printObj(newList)#should be blank
print("New List Populated")
tupleToList(myFavsTuple, newList)
printObj(newList)
print(newList)
