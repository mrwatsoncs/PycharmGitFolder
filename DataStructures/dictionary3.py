#create a dictionary of 5 items with a dictionary within
#the key will be an item number
#the dicionary within will have several items
#each item within should have an itemName, itemPrice, and itemQuant

groceryStore = {
    1: {
        'itemName': 'apple',
        'itemPrice': 6,
        'itemQuant': 10
    },

    2: {
        'itemName': 'orange',
        'itemPrice': 2,
        'itemQuant': 5
    },

    3: {
        'itemName': 'grapes',
        'itemPrice': 6,
        'itemQuant': 8
    },

    4: {
        'itemName': 'banana',
        'itemPrice': 1,
        'itemQuant': 10
    },

    5: {
        'itemName': 'mango',
        'itemPrice': 3,
        'itemQuant': 5
    }
}

#variable to hold the value of all items in our shopping cart
grandTotal = 0

#an empty list to add items that we wish to purchase
shoppingCart = []

# EASY
# function that takes in items to add to our cart
# reduces the quantity of items we are buying
# def addToCart(itemNum, howMany):
#     # global shoppingCart
#     #iterates 'howMany' times
#     #adds the item number each time
#     for i in range(0, howMany):
#         shoppingCart.append(groceryStore[itemNum])
#     #deduct items from groceryStore
#     groceryStore[itemNum]['itemQuant'] -= howMany
#     # groceryStore[itemNum]['itemQuant'] = groceryStore[itemNum]['itemQuant'] - howMany
#     #print what we have
#     print('We have added {} {}s to our cart'.format(howMany, groceryStore[itemNum]['itemName']))
#     #print what is leftover
#     print('There are {} {}s leftover'.format(groceryStore[itemNum]['itemQuant'],groceryStore[itemNum]['itemName']))
#
# addToCart(1, 5) #added 5 apples to cart, 5 leftover


# MEDIUM
# supply the function with an item name and quant
def addToCart(itemName, howMany):
    #counter for items to add
    addItems = 0
    #while loop for adding items
    while(addItems < howMany):
        for i in groceryStore:
            #when the item we pass as an argument
            #matches the item in our grocery store
            #add it to the cart
            if groceryStore[i]['itemName'] == itemName:
                itemFound = i
                shoppingCart.append(groceryStore[i])
                groceryStore[i]['itemQuant'] -= 1
                #update counter
                addItems += 1
                #addItems = addItems + 1
    print('We have added {} {}s to our cart'.format(howMany, groceryStore[itemFound]['itemName']))
    # print what is leftover
    print('There are {} {}s leftover'.format(groceryStore[itemFound]['itemQuant'],groceryStore[itemFound]['itemName']))

addToCart('mango', 2) # added two, 3 leftover


#DIFFICULT
#same as before, but this function
#must also check if item exists
#error if it does not
# def addToCart(itemName, howMany):
#     hasItem = False
#     addItems = 0
#     for i in groceryStore:
#         if itemName in groceryStore[i]['itemName']:
#             hasItem = True
#             if(howMany > groceryStore[i]['itemQuant']):
#                 print('Sorry! We dont have enough left! ({}) Please add another amount {} or less'.format(itemName, groceryStore[i]['itemQuant']))
#             if(howMany <= groceryStore[i]['itemQuant']):
#                 while(addItems < howMany):
#                     for j in groceryStore:
#                         if groceryStore[j]['itemName'] == itemName:
#                             shoppingCart.append(groceryStore[j])
#                             groceryStore[j]['itemQuant'] -= 1
#                             addItems += 1
#                 print('We have added {} {}s to our cart'.format(howMany, groceryStore[i]['itemName']))
#
#     if(hasItem == False):
#         print('Sorry! {} is not available'.format(itemName))

addToCart('apple', 3) #line 100 print statement
# addToCart('watermelon', 1) #line 111 print statement
addToCart('orange', 5)
addToCart('banana', 2)
addToCart('grapes', 1)
print()
print('---checkout---')
#prints a tally and total price of our items
def checkOut():
    global grandTotal
    # global shoppingCart
    for i in range(0, len(shoppingCart)):
        grandTotal += shoppingCart[i]['itemPrice']
        print('{}: {}'.format(shoppingCart[i]['itemName'], shoppingCart[i]['itemPrice']))
    print('Your Total is ${}'.format(grandTotal))

checkOut()
