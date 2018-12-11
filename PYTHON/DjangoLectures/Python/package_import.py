#import package
# import package_import1
# package_import1.my_func()

#give a short alias name to imported package
# import package_import1 as pkg1
# pkg1.my_func()

#import specif function from package
# from package_import1 import my_func
# my_func()

#import everything from package but not recomended since it uses more memory
from package_import1 import *
my_func()
