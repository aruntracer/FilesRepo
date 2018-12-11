import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(__file__) #settings.py
print(os.path.abspath(__file__)) #D:\EDrive\Python\python\DjanoLectures\DjangoEnv1\first_pro\first_pro\settings.py
print(os.path.dirname(os.path.abspath(__file__))) #D:\EDrive\Python\python\DjanoLectures\DjangoEnv1\first_pro\first_pro
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #D:\EDrive\Python\python\DjanoLectures\DjangoEnv1\first_pro
print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) #D:\EDrive\Python\python\DjanoLectures\DjangoEnv1

#to concatenate the paths we need to use os.path.join keyword
print(os.path.join(BASE_DIR,"folder")) #D:\EDrive\Python\python\DjanoLectures\folder
