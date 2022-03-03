# in Py we can define a funcion without name, this is anonymous function or lamda function

# lambda function

from re import X
from unittest import result


square = lambda x: x * x

# function call
result = square(5)
print(result)

# this program equivalent to:


def square(x):
    return x * x


result = square(5)

print(result)

# lambbda function

sum = lambda a, b, c: a + b + c
print(sum(1, 2, 4))


