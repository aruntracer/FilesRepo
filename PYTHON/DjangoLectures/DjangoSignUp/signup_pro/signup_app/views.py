from django.shortcuts import render
from signup_app.forms import NewUser

def index(request):
    return render(request,'signup_app/index.html')
def users(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')
    return render(request,'signup_app/users.html',{'form':form})
