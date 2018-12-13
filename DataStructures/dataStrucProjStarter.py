#DO NOT DELETE THE FOLLOWING LINE
import getpass


isLoggedIn = False
currUser = ""


bankUsers = {
    1: {
        'user_name': 'John',
        'pinNum': 1234,
        'balance': 100
    }
}


def login():
    #*** SIMILAR TO DICTIONARY 3 MEDIUM ADDTOCART()***
    #take user input and store it as variable
    #for loop
        #check if that input equals the bankUser[i]['pinNum']
        #if pin is correct
            #run bankApp()

    print('login')
    bankApp()

#deposit
def deposit():
    #global currUser
    print('deposit')
    #take an amount from user input
    amt = input('How much would you like to deposit?')

    #check amt to make sure it is less than 1000 and greater than 0
    #if amt is less than 1000 and amt is greater than 0
    if(int(amt) < 999 and int(amt) > 0):

        #update current users balance
        #currUser['balance'] += amt
        currUser['balance'] += int(amt)
 

#withdraw
def withdraw():
    print('withdraw')
    #take an amount from user input
    wdAmt = input('How much would you like to withdraw?')

    #check amt to make sure it is less than users balance
    #if amt is less than currUser['balance']

        #update current users balance
        #currUser['balance'] -= amt

#checkBalance
def checkBalance():
    print('check balance')

#logout
def logout():
    print('logout')

def bankApp():
    #starter code..
    operation = input('(1) Deposit Funds, (2) Withdraw Funds, (3) Check Account Balance, (4) Logout\n')
    if(int(operation) == 1):
        deposit()
    elif(int(operation) == 2):
        withdraw()
    elif(int(operation) == 3):
        checkBalance()
    elif(int(operation) == 4):
        logout()
    else:
        print('\nSorry, that operation is not valid, please select an input from 1-4\n')


print('Welcome to Watson Funds Bank!')
print('Login to begin\n')
login()
