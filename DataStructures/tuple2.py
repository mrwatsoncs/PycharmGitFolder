myTuple = ('Patriots', 'Suns', 'Team USA', 'Blackhawks', 'Yankees')
# create a function tupleRemove that removes an item from a tuple
# change it into a list
# remove the item from the list
# return a new tuple

def tupleRemove(tup, item):
    #created a blank list
    mList = []
    #iterated over the tuple and added
    #items to the list
    for i in tup:
        mList.append(i)
    #removed unwanted item from list
    mList.remove(item)
    #changed our list back to a tuple
    newTuple = tuple(mList)
    return newTuple

def printObj(obj):
    for i in obj:
        print(i, end=' ')
    print('')


print("Print original tuple")
printObj(myTuple)#everything from our original tuple
print()
print("Tuple after removed item")
printObj(tupleRemove(myTuple, 'Patriots'))#everything besides patriots
print(tupleRemove(myTuple, 'Patriots'))
