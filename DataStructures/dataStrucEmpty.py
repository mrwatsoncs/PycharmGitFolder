
#user, pin, balance
users = {
    1: {'name': 'Sean', 'pin': 2231, 'balance': 100, 'role': 'manager'},
    2: {'name': 'Addy', 'pin': 1367, 'balance': 100, 'role': 'standard'},
    3: {'name': 'Mason', 'pin': 8796, 'balance': 100, 'role': 'standard'},
    4: {'name': 'Molly', 'pin': 5379, 'balance': 100, 'role': 'standard'}
}

#receipt
receipt = []

#login function
def login():
    global users
    global loggedInStatus
    global loggedInUser
    loggedInStatus = False
    pin = int(input('Please enter your unique PIN.\n'))
    for user, info in users.items():
        if pin == info['pin']:
            loggedInStatus = True
            loggedInUser = users[user]
    if loggedInStatus == False:
        print('\nThe pin you entered is invalid.\n')
        login()

#deposit function
def deposit():
    global users
    global receipt
    global loggedInUser
    amount = int(input('\nHow much money would you like to deposit?\n$'))
    if amount > 0 and amount < 1000:
        loggedInUser['balance'] += amount
        receipt.append('Deposit: ${}'.format(amount))
        print('\n${} has been deposited into your account.\n'.format(amount))
    elif amount >= 1000:
        print('\nThe number you entered is too high.')
        deposit()
    elif amount <= 0:
        print('\nThe number you entered is too low')
        deposit()
    else:
        print('\nThe number you entered is invalid.')
        deposit()
    bankApp()

#withdraw function
def withdraw():
    global users
    global receipt
    global loggedInUser
    amount = int(input('\nHow much money would you like to withdraw?\n$'))
    if amount < loggedInUser['balance']:
        loggedInUser['balance'] -= amount
        receipt.append('Withdraw: ${}'.format(amount))
        print('\n${} has been withdrawn from your account.\n'.format(amount))
    elif amount == loggedInUser['balance']:
        print('\nThe number you entered is equal to your current balance.')
        withdraw()
    elif amount > loggedInUser['balance']:
        print('\nThe number you entered is greater than your current balance.')
        withdraw()
    else:
        print('\nThe number you entered is invalid.')
        withdraw()
    bankApp()

#checkbalance function
def checkBalance():
    global users
    global loggedInUser
    print('\nYour current balance is ${}.\n'.format(loggedInUser['balance']))
    bankApp()

#viewreceipt function
def viewReceipt():
    global receipt
    print('')
    if len(receipt) > 0:
        for transaction in receipt:
            print(transaction)
    else:
        print('You have not made any transactions.')
    print('')
    bankApp()

#addnewuser function
def addNewUser():
    global users
    newName = str(input('\nName:\n'))
    newPin = int(input('\nPIN:\n'))
    newRole = str(input('\nStandard or manager:\n'))
    if newRole == 'Standard' or role == 'standard':
        newRole = 'standard'
    elif newRole == 'Manager' or role == 'manager':
        newRole = 'manager'
    else:
        newRole = 'standard'
    users[len(users)+1] = {'name': newName, 'pin': newPin, 'balance': 100, 'role': newRole}
    bankApp()

#printallusers function
def printAllUsers():
    global users
    for user, info in users.items():
        print('')
        for key in info:
            print('{}: {}'.format(key, info[key]))
    print('')
    bankApp()

#logout function
def logout():
    print('\nThank you for using our service!')
    exit()

#standardbankapp function
def standardBankApp():
    print('Transactions:')
    print('1) Deposit')
    print('2) Withdraw')
    print('3) Check Balance')
    print('4) View Receipt')
    print('5) Log Out')
    transaction = int(input('\nWhat number transaction would you like to perform?\n'))
    if transaction == 1:
        deposit()
    elif transaction == 2:
        withdraw()
    elif transaction == 3:
        checkBalance()
    elif transaction == 4:
        viewReceipt()
    elif transaction == 5:
        logout()
    else:
        print('\nThe number you entered is invalid.\n')
        standardBankApp()

#managerbankapp function
def managerBankApp():
    print('Transactions:')
    print('1) Deposit')
    print('2) Withdraw')
    print('3) Check Balance')
    print('4) View Receipt')
    print('5) Add New User')
    print('6) Print All Users')
    print('7) Log Out')
    transaction = int(input('\nWhat number transaction would you like to perform?\n'))
    if transaction == 1:
        deposit()
    elif transaction == 2:
        withdraw()
    elif transaction == 3:
        checkBalance()
    elif transaction == 4:
        viewReceipt()
    elif transaction == 5:
        addNewUser()
    elif transaction == 6:
        printAllUsers()
    elif transaction == 7:
        logout()
    else:
        print('\nThe number you entered is invalid.\n')
        managerBankApp()

#bankapp function
#determines what bankapp function to use
def bankApp():
    global users
    global loggedInUser
    if loggedInUser['role'] == 'manager':
        managerBankApp()
    else:
        standardBankApp()

login()
print('\nWelcome {}!\n'.format(loggedInUser['name']))
bankApp()
