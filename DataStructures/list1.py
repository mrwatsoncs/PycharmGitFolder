nameList = ['John', 'Felix', 'Maurice', 'Adrian']

#a line for spacing
def line():
    print('\n---------------')

# create a for..in loop that prints the entire list
for i in nameList:
    print(i)

line()
# create 4 total print statements
# print each name (using its index)
print(nameList[0])
print(nameList[1])
print(nameList[2])
print(nameList[3])


line()
# create a statement that prints the index
# of the third name on your list
print("Maurice is at index ", nameList.index("Maurice"))


line()
# create a print statement that prints
# the length of your list
print("The length of my list is", len(nameList))


line()
# create a function 'printList' that prints
# the entire list
def printList():
    print("Here is our list!")
    for name in nameList:
        print(name)

printList()

line()
# add three names to the list, using .append()
# print the list using printList()
nameList.append('Malik')
nameList.append('Kenneth')
nameList.append('Jarvis')

printList()


line()
#using remove() remove the first two names of your lst
#print the list

nameList.remove('John')
nameList.remove('Felix')

printList()

line()
#using the del keyword, remove the last name on your list
del nameList[len(nameList)-1]

printList()

line()
print('function option 1')
def welcomeMessage():
    for name in nameList:
        print('Hello', name + '!')

welcomeMessage()

line()
print('function option 2')
def sayHello(list):
    for i in list:
        print('Hello,', i, 'from our second function!')

sayHello(nameList)
