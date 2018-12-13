#Mr Watson
#functions5.py

def myName():
    return "Mr Watson"

def myFav():
    return "Maroon"

def myHobby():
    return "Playing Basketball"

# print (myName())
# print (myFav())
# print (myHobby())

def f2c(fTemp):
    cTemp = ((fTemp -32) * 5/9)
    return cTemp

# print (f2c(32))

def maxNum(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

def minNum(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

# print (maxNum(2, 5, 723))
# print (minNum(6, 243000, 5))

def combineNum(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z






print (maxNum(2, 5, 723))
print (minNum(6, 243000, 5))

print(combineNum(maxNum(1,2,3), "+", minNum(5, 6, 7)))
# print(combineNum(3, "+", 5))


















