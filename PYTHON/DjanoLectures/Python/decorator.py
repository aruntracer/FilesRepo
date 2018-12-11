#if a variable referenced inside a function is not present inside it then it will check for global variable
s = "Global Variable"
def func():
    print(s)

func()
#op Global Variable

#function will check for variable inside the function first
def func1():
    s = 10
    print(s)

func1()
print(s)
#op Global Variable
#op 10

#modify global variable inside a function
def func2():
    global s
    s = 10
    print(s)

func2()
print(s)
#op 10
#op 10

