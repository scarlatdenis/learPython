from tkinter import Y


def func():
    x = 10
    print("Vlue of x inside funtion: ", x)


x = 20
func()
print("Value outside function: ", x)

##############################################
def func1():
    a = 5


func1()
print(a)  # error, a is not defined, is out of scope
