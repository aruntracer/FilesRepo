x = 25

def my_func():
    x = 33
    def myf1():
        print(x)
    myf1()
my_func()
print(x)


x = 60

def g_func():
    global x
    x = 99
print("before fn call" + x)
g_func()
print("after fn call" + x)
