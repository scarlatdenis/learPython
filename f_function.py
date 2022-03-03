

def greet(name):
    print("Hello", name)
    print("What`s going on?")
greet("Paul")
#the first function


def summ(n1, n2):
    sum = n1 + n2
    print("The summ of numbers is: ", sum)

summ(5,12)

def get_absolute(num):
    if num >= 0:
        return num
    else:
        return - num
print(get_absolute(10))
print(get_absolute(-11))
print(get_absolute(-23))
