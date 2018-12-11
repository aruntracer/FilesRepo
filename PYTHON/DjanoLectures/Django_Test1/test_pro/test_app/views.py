from django.shortcuts import render
from test_app.models import users

# Create your views here.
def index(request):
    return render(request,'test_temp/index.html')

def user(request):
    users_obj = users.objects.order_by('first_name')
    users_dict = {'user_records':users_obj}
    return render(request,'test_temp/users.html',context=users_dict)
