import getpass


isLoggedIn = False
currUser = ""
loginAttempts = 0
validOp = True

bankUsers = {
    1: {
        'user_name': 'John',
        'pinNum': 1234,
        'balance': 100,
        'transactions': [],
        'isManager': True
    },
    2: {
        'user_name': 'Beth',
        'pinNum': 1234,
        'balance': 100,
        'transactions': [],
        'isManager': False
    },
    3: {
        'user_name': 'Leah',
        'pinNum': 1234,
        'balance': 100,
        'transactions': [],
        'isManager': False
    },
    4: {
        'user_name': 'Roger',
        'pinNum': 1234,
        'balance': 100,
        'transactions': [],
        'isManager': False
    },
    5: {
        'user_name': 'Ronald',
        'pinNum': 1234,
        'balance': 100,
        'transactions': [],
        'isManager': False
    },
}

#login
#loops username input until valid
#loops pin input until valid
#starts bankApp()
def login():
    global currUser, loginAttempts, bankUsers
    pinAttempts = 0
    validUser = False
    validPin = False
    while(loginAttempts < 5):
        if(validUser == False):
            userName = input('Please enter your user name:\n')
            for i in bankUsers:
                if(bankUsers[i]['user_name'].lower() == userName.lower()):
                    validUser = True
                    currUser = bankUsers[i]
                    break
            else:
                loginAttempts+=1
                if(loginAttempts < 5):
                    print('Sorry, please enter a valid user name\n')
        elif(validUser):
            while(pinAttempts < 5):
                userPin = input('\n{}, please enter your pin\n'.format(currUser['user_name']))
                # userPin = getpass.getpass('\n{}, please enter your pin\n'.format(currUser['user_name']))
                if(userPin != str(currUser['pinNum'])):
                    pinAttempts+=1
                    if(pinAttempts < 5):
                        print('\nInvalid pin!')
                elif(userPin == str(currUser['pinNum'])):
                    print('\nWelcome to Watson Funds Bank!\n')
                    print('How can we assist you today? (Enter the number of your choice)')
                    validPin = True
                    break
            if(pinAttempts == 5):
                print('\nToo many unsuccessful attempts, please try again later!')
                return
            if(validPin):
                break
    if(loginAttempts == 5):
        print('\nToo many unsuccessful attempts, please try again later!')
    if(validPin):
        bankApp()


#deposit
def deposit():
    global validOp
    validDeposit = False
    completedDeposit = False
    depositErrCounter = 0
    depositErrCounter2 = 0
    depositErrCounter3 = 0
    print('\n------Deposit------\n')
    while(validDeposit == False):
        amt = input('How much would you like to deposit?\n')
        if(amt.isdigit()):
            if(int(amt) < 999 and int(amt) > 0):
                currUser['balance'] += int(amt)
                print('\nGreat! Your new balance is ${}\n'.format(currUser['balance']))
                validDeposit = True
                currUser['transactions'].append('Deposit: $' + str(amt))
                # print(currUser['transactions'])
            else:
                print('Invalid deposit amount, please try again\n')
                depositErrCounter += 1
                if (depositErrCounter == 5):
                    print('An error has occured, your transaction has been cancelled')
                    validOp = False
                    return
        elif(amt.isdigit() == False):
            print('Deposit not accepted, please try again\n')
            depositErrCounter2 += 1
            if (depositErrCounter2 == 5):
                print('An error has occured, your transaction has been cancelled')
                validOp = False
                return
    while(completedDeposit == False):
        finished = input('Would you like to complete another transaction? Y/N\n')
        if(finished.lower() == 'y'):
            completedDeposit = True
            bankApp()
        elif(finished.lower() == 'n'):
            print('\nThank you for using Watson Funds Bank!')
            completedDeposit = True
            validOp = False
            receipt()
            break
        else:
            print('Invalid Input\n')
            depositErrCounter3+=1
            if(depositErrCounter3 == 5):
                print('An error has occured, your transaction has been cancelled')
                validOp = False
                return


#withdraw
def withdraw():
    global validOp
    validWithdraw = False
    completedWithdraw = False
    withdrawErrCounter = 0
    withdrawErrCounter2 = 0
    withdrawErrCounter3 = 0
    print('\n------Withdraw------\n')
    while(validWithdraw == False):
        amt = input('How much would you like to withdraw?\n')
        if(amt.isdigit()):
            if(int(amt) < currUser['balance'] and int(amt) > 0):
                currUser['balance'] -= int(amt)
                print('\nAwesome! Your new balance is ${}\n'.format(currUser['balance']))
                validWithdraw = True
                currUser['transactions'].append('Withdraw: $' + str(amt))
                # print(currUser['transactions'])
            else:
                print('Insufficient funds, please try again\n')
                withdrawErrCounter += 1
                if (withdrawErrCounter == 5):
                    print('An error has occured, your transaction has been cancelled')
                    validOp = False
                    return
        elif(amt.isdigit() == False):
            print('Withdraw not accepted, please try again\n')
            withdrawErrCounter2 += 1
            if (withdrawErrCounter2 == 5):
                print('An error has occured, your transaction has been cancelled')
                validOp = False
                return
    while(completedWithdraw == False):
        finished = input('Would you like to complete another transaction? Y/N\n')
        if(finished.lower() == 'y'):
            completedWithdraw = True
            bankApp()
        elif(finished.lower() == 'n'):
            print('\nThank you for using Watson Funds Bank!')
            completedWithdraw = True
            validOp = False
            receipt()
            break
        else:
            print('Invalid Input\n')
            withdrawErrCounter3 += 1
            if (withdrawErrCounter3 == 5):
                print('An error has occured, your transaction has been cancelled')
                validOp = False
                return

#checkBalance
def checkBalance():
    global validOp
    print('\n-----{}\'s Balance------'.format(currUser['user_name']))
    print('${}.00\n'.format(currUser['balance']))
    # validOp = False

#addNewUser
def addNewUser():
    global validOp
    validUserName = False
    validPin = False
    validBalance = False
    validNewUser = False
    print('\n-----Manager Options - Add New User // {}-----'.format(currUser['user_name']))
    while(validNewUser == False):
        while(validUserName == False):
            userName = input('Enter user name: ')
            if(userName.isdigit()):
                print('Invalid Username')
                break
            else:
                thisUserName = userName
                validUserName = True
                break
        if(validUserName):
            while(validPin == False):
                pin = input('Enter pin: ')
                if(pin.isdigit() == False):
                    print('Invalid Pin')
                    break
                if(pin.isdigit()):
                    thisPin = pin
                    validPin = True
                    break
        if(validPin):
            while(validBalance == False):
                balance = input('Enter initial deposit: ')
                if(balance.isdigit() == False):
                    print('Invalid Balance Input')
                    break
                if(balance.isdigit()):
                    thisBalance = balance
                    validBalance = True
                    break
        if(validBalance):
            newUserIndex = len(bankUsers)+1
            validNewUser = True
    if(validNewUser):
        bankUsers[newUserIndex] = {
            'user_name': thisUserName,
            'pin': thisPin,
            'transactions': [],
            'isManager': False
        }
        print('New User {} has been added!\n'.format(bankUsers[newUserIndex]['user_name']))
        # validOp = False

#print all users
def printAllUsers():
    print('\n-----Manager Options - Print Add Users // {}-----\n'.format(currUser['user_name']))
    for i in bankUsers:
        print('Bank User {}: {}'.format(i, bankUsers[i]['user_name']))
    print()


#logout
def logout():
    global validOp
    print('\nThank you for using Watson Funds Bank!')
    receipt()
    validOp = False

#printReciept
def receipt():
    printReciept = True
    receiptCounter = 0
    while(printReciept):
        receipt = input('Would you like a receipt? Y/N\n')
        if(receipt.lower() == 'y'):
            print('\n-----{}\'s Receipt------'.format(currUser['user_name']))
            if(len(currUser['transactions']) > 0):
                for i in range(0, len(currUser['transactions'])):
                    print(currUser['transactions'][i])
                print('\n-----\nBalance: ${}'.format(currUser['balance']))
                return
            else:
                print('No transactions!')
                return
        elif(receipt.lower() == 'n'):
            print('\nHave a great day!')
            return
        else:
            print('Invalid Input')
            receiptCounter+=1
            if(receiptCounter == 5):
                print('An error has occured, your transaction has been cancelled')
                return

def bankApp():
    global currUser, validOp
    while(validOp):
        operation = input('(1) Deposit Funds, (2) Withdraw Funds, (3) Check Account Balance, (4) Logout\n')
        if(int(operation) == 1):
            deposit()
        elif(int(operation) == 2):
            withdraw()
        elif(int(operation) == 3):
            checkBalance()
        elif(int(operation) == 4):
            logout()
            return
        elif(int(operation) == 5):
            if(currUser['isManager']):
                addNewUser()
            else:
                print('\nYou are not authorized to perform this action\n')
        elif(int(operation) == 6):
            if(currUser['isManager']):
                printAllUsers()
            else:
                print('\nYou are not authorized to perform this action\n')
        else:
            print('\nSorry, that operation is not valid, please select an input from 1-4\n')


print('Welcome to Watson Funds Bank!')
print('Login to begin\n')
login()
