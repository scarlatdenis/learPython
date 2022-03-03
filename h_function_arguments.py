from unicodedata import name


def greet(name, msg):
    print("Hello " + name + ", " + msg)


# greet("Monica")

# error, missing msg, but we can set default arguments msg in function


def greet2(name, msg="How are you?"):
    print("Hello " + name + ", " + msg)


greet2("Suzana")
greet2("Marcelino", "Are you kidding me?")


def greet3(name, msg):
    print("Hello " + name + ", " + msg)


greet3(
    msg="Wats`up teeneger?", name="Klimili"
)  # we can write aguments that    <=====  Mix it


# Py Arbitrary arguments


def arbitrary(*names):
    print(names)


arbitrary("Maria, Ioana, Marihuanna")
