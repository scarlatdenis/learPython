from itertools import product


class MyClass:
    a = 10

    def func(self):
        return "Hello"


# instantiate an object
ob = MyClass()

print(ob.func())  # Output: 'Hello'
print(ob.a)  # Output: 10


# another class


class Number:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


n1 = Number()

sum = n1.add(2, 3)
print(sum)

product = n1.multiply(2, 5)
print(product)


