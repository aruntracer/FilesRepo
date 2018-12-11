def hello(name = 'nive'):
    print('name is '+name)

hello() #op name is nive
print(hello) #op <function hello at 0x0000010DA14BC1E0>
name = hello
name() #op name is nive

#function wihtin functions and returning functions
def main_func(name = 'nive'):
    print('main func run')
    def in_func():
        return 'this is in in_func'
    def in_func1():
        return 'this is in in_func1'
    print(in_func())
    print(in_func1())
    if name == 'nive':
        return in_func()
    else:
        return in_func1()
print(main_func('name1'))
