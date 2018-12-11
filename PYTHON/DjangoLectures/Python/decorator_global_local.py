s = 'global variable'

#check global and local variables
def func3():
    var_infunc = 10
    print(globals())
    print('\n')
    print(locals())
    print('\n')
    print(globals()['s'])

func3()
'''op
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001DF67B18550>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:/EDrive/Python/python/DjanoLectures/decorator_global_local.py', '__cached__': None, 's': 'global variable', 'func3': <function func3 at 0x000001DF67ACC1E0>}


{'var_infunc': 10}


global variable
'''
