import os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_pro.settings')
django.setup()

from test_app.models import users
# from random import choice

fnames = ['arun','nive','ramya','divya','janani']
lnames = ['kumar','jayapathy','guna','alex','sriram']

# for acc in range(4):
#     user_obj = users(first_name=choice(fnames)+str(acc),last_name=choice(lnames)+str(acc),Email=choice(fnames)+str(acc)+"@gmail.com")
#     user_obj.save()

# print(users.objects.all())
# print(users.objects.first())
# print(users.objects.last())
print(users.objects.filter(first_name="ramya"))
users = users.objects.all()

for user in users:
    print(user.first_name)
    print(user.last_name)
    print(user.Email)
