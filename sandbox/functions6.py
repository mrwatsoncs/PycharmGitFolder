# Mr Watson
#functions6.py
# volume = area * height
# area = pi*(r**2)/(r^2)
area = 0
height = 0
volume = 0

def cylVolume(r, h):
    global area
    global height
    global volume
    area = 3.14*(r**2)
    height = h
    volume = area*height
    return volume

print(cylVolume(3, 5))

def area(r):
    global area
    area = 3.14*(r**2)
    return area

def cylVolume2(a, h):
    global volume
    global height
    height = h
    volume = a*height
    return volume

print(area(3))
# print(cylVolume2(area(3), 5))
