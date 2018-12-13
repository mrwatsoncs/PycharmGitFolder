numList = [5, 10, 20, 30]

def line():
    print('------------\n')

def printList(list):
    for i in list:
        print(i)

printList(numList)

#delete a number from the list, print the list
line()
del numList[0]
del numList[0]

printList(numList) #20, 30

#create a function 'addFive' that adds five
#to each number. Print the list
line()
def addFive(list):
    for i in list:
        i += 5
        # i = i + 5
        print(i)

addFive(numList) #25, 35

#create a function 'multNum' that multiplies
#all the numbers together
line()
def multNum(list):
    result = 1
    for i in list:
        result *= i
    return result

print(multNum(numList)) #20*30 = 600

#add 5 numbers to the list
numList.append(40)
numList.append(-600)
numList.append(50)
numList.append(60)
numList.append(-50)
numList.append(-100)


line()
printList(numList)

#create a function 'minNum' that returns the
#smallest number in the list
line()
def minNum(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

# myList = [20, 30, 40, -600, 50, 60, -50, -100]
print(minNum(numList)) #-100

#create a function 'maxNum' that return
#the largest number in the list
line()
def maxNum(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

print(maxNum(numList)) #60


line()
def addCommas(num):
    commaNum = str(num)
    commaCount = len(commaNum)
    for i in commaNum:
        print(i, end='')
        commaCount -= 1
        if commaCount%3 == 0 and commaCount > 0:
            print(",", end='')

addCommas(154635835135743517419698435468765468)
