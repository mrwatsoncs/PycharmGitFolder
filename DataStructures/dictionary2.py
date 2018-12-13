def line():
    print('\n---------------\n')

class_roster_dictionary = {1: {'name': 'Matthew', 'age': 15, 'favSubject': 'Math'}, 2: {'name': 'Jessica', 'age': 15, 'favSubject': 'English'}}

class_roster_dictionary2 = {1: {'name': 'Matthew', 'age': 15, 'favSubject': 'Math'},
                            2: {'name': 'Jessica', 'age': 15, 'favSubject': 'English'}}

class_roster = {
    1: {
        'name': 'Matthew',
        'age': 15,
        'favSubject': 'Math'
    },
    2: {
        'name': 'Jessica',
        'age': 15,
        'favSubject': 'English'
    }
}

#print the first item of class_roster
print('First item of class roster')
print(class_roster[1])

#print ONLY the name of the first student
line()
print('name of first student')
print(class_roster[1]['name'])#matthew

#print each item of the dictionary using .format()
line()
print('Each dictionary item')
for i in class_roster:
    name = class_roster[i]['name']
    age = class_roster[i]['age']
    fav = class_roster[i]['favSubject']
    print('{} is {} years old and loves {}'.format(name, age, fav))


#create a function to print our class roster
line()
print('Class Roster function')
def printClassRoster():
    for i in class_roster:
        name = class_roster[i]['name']
        age = class_roster[i]['age']
        fav = class_roster[i]['favSubject']
        print('{} is {} years old and loves {}'.format(name, age, fav))

printClassRoster()


#change matthews favorite subject to CS
line()
print('Matthew\'s new Fav Subject')
class_roster[1]['favSubject'] = 'Computer Science'

printClassRoster()

#Increase Jessicas age by 1
line()
print('Happy Birthday Jessica')
class_roster[2]['age'] = class_roster[2]['age']+1
# class_roster[2]['age'] += 1
printClassRoster()

#add totalClasses to each object, set it to 5
for i in class_roster:
    class_roster[i]['totalClasses'] = 5

def newPrintClassRoster():
    for i in class_roster:
        name = class_roster[i]['name']
        age = class_roster[i]['age']
        fav = class_roster[i]['favSubject']
        total = class_roster[i]['totalClasses']
        #{} is {} years old. They have {} classes and loves {} the most!
        print('{} is {} years old. They have {} classes and loves {} the most!'.format(name, age, total, fav))

line()
print('New print class roster')
newPrintClassRoster()

#***** BONUS *******
line()
print("BONUS")
fake_class_roster =  {
    1: {
        'name': 'Matthew',
        'age': 15,
        'favSubject': 'Math',
        'subjectList': ['Math', 'English', 'Science']
    },
    2: {
        'name': 'Jessica',
        'age': 15,
        'favSubject': 'English',
        'subjectList': ['Math', 'English', 'Science']
    }
}

for i in fake_class_roster:
    fake_class_roster[i]['subjectList'].append('PE')
    fake_class_roster[i]['totalClasses'] = len(fake_class_roster[i]['subjectList'])

for i in fake_class_roster:
    name = fake_class_roster[i]['name']
    age = fake_class_roster[i]['age']
    fav = fake_class_roster[i]['favSubject']
    total = fake_class_roster[i]['totalClasses']
    print('{} is {} years old. They have {} classes and loves {} the most!'.format(name, age, total, fav))


