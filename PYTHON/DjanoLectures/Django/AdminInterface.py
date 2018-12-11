'Can configure our model in Admin interface instead of Python shell'
'First register the app in admin.py'
    '''
        from django.contrib import admin
        from first_app.models import AccessRecord,Topic,Webpage

        # Register your models here.
        admin.sites.register(Topic)
        admin.sites.register(Webpage)
        admin.sites.register(AccessRecord)
    '''
'Create a admin superuser'
    'run python manage.py createsuper'
'runserver and give /admin in the url to login to adming page'
