#create a project Django using django-admin
'''run "django-admin startproject proj_name" in cmd'''

#Starting Django server
'''run "python manage.py runserver [IPADDRESS:PORT] [PORT]" in cmd in project location where manage.py is present to start the django server'''
    'New ipaddress needs to be added in ALLOWED_HOSTS = ['192.168.26.25',] in settings file'

#Creating our app
'''django-admin startapp anyappname'''
'or'
'''run "python manage.py startapp anyappname(first_app)"'''

#settings.py
'''INSTALLED_APPS'''
    '''contains the entry for our created app in project used to tell django that to consider our to run in server'''
    '''first_app'''
'''TEMPLATES'''
    '''TEMPLATES is a dictionary which contains various info required for django'''
    '''configure the paths which we need to access in this came the path of the templates folder which contains the html files'''
'''STATIC_URL STATICFILES_DIRS'''
    '''STATIC_URL is mentioned to indicate django to read static files'''
    '''STATICFILES_DIRS is a dictionary which contains urls where to look for static files in project eg. images css javasripts etc'''
    '''create a folder named static this is must else it wont work with different name and put all staticfiles in it'''
#views.py
'''sends data to browser'''
'''contains the view for our web app like index, home etc'''
'''can also create a function for index view and send data to browser'''
'''each view must respond an HttpResponse object'''
'''to see this view in our servers we need to map this view in urls.py file'''
'''use render from django.shortcuts to read html files and present to browser'''
    '''in html file use {{variable_name}} to get the data from views.py'''
    '''in views.py create a dictionary for the variable_name's in the html file and assign values to it'''
        '''my_dict = {'variable_name':"Hello I am from views.py !",'variable_name2':"I'm hello"}'''
    '''in views.py return the html file using render'''
        '''return  render(request,'index.html',context=my_dict)'''#here request is the in parameter and index.html indicates django to search the html files in DIR's mentioned in settings TEMPLATES dictionaries and context contains the dictionaries which needs to be sent/inject to html files

#urls.py
'''urlpatterns'''
    '''contains the mapping for views'''
    '''path('index/',views.index,name='index') --will show index functions output in browser if we put --http://127.0.0.1:8000/index/'''
    '''path('first_app/', include('first_app.urls')), --here we use include keyword to search for urls in the specified path, --http://127.0.0.1:8000/first_app/'''
    '''path('',views.index,name='index') --http://127.0.0.1:8000/'''

#__init__.py
'''blank python script which indicates this is package by its special name'''

#wsgi.py
'''acts as a web server gateway interface'''
#manage.py
'''associated with many commands'''

#Migrations
'''allows you to move database from one design to another and vice versa'''

'''a folder will be created with the appname'''

#__init__.py

#admins.py

#apps.py

#models.py

#tests.py

#Adding our app to django server
'''go to setting.py file of our project in INSTALLED_APPS add our app name in it'''
'''now django will know that our app exists'''

'''Misc'''
    '''
    In Html {{}} is used to mention any variable which is declared in views.py function and you want to use here {{ insert_me }}
        and {%%} is used to mention any path to static files <img src="{%static "/images/r1.jpg"%}" alt="Oops Images Not Loaded!">   <link rel="stylesheet" href="{%static "/css/style.css"%}">
    '''
'So Far we have seen templates and views in Django'
'-----------------TEMPLATES AND VIEWS ends-----------------'
