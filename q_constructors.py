# construcor is special functions with double underscore like this:  __function__().
# this function called whenever a new object of that class

# Example:


class MyClass:
    def __init__(self, p1=0, p2=0):
        self.a = p1
        self.b = p2


o1 = MyClass(2, 3)

print(o1.a, o1.b)

o2 = MyClass()
print(o2.a, o2.b)


# another example


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5


p1 = Point(6, 8)
distance = p1.distance()

print(distance)  # Output: 10

# another example


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(6, 8)

# Output: (6, 8)
print((p1.x, p1.y))

# deleting y attribute of the p1 object
del p1.y

print(p1.x)  # Output: 6

# AttributeError: 'Point' object has no attribute 'y'
print(p1.y)

# another


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(6, 8)

# Output: <__main__.Point object at 0x7f92330cc208>
print(p1)

# deleting the p1 object
del p1

# NameError: name 'p1' is not defined
print(p1)

