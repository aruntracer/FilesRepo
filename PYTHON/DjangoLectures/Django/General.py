'''
Make a python file inside django project and Configure it for running django using our projects settings.py
'''
import os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','db_project.settings')
django.setup()

from django.contrib.auth.models import User

print(User.objects.all())
''
