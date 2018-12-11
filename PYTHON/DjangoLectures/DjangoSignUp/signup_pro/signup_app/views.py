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
            form_dict = {'user_name':form.cleaned_data['first_name']}
            return success(request,form_dict)
        else:
            print('Error form invalid')
    return render(request,'signup_app/users.html',{'form':form})
def success(request,form_dict):
    print('Name is '+form_dict['user_name'])
    return render(request, 'signup_app/success.html',context=form_dict)
