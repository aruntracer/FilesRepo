from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'welcome_text':"Welcome to index page"}
    return render(request,'second_app/index.html',context=my_dict)

def help_fn(request):
    my_dict = {'help_text':"Welcome to help page"}
    return render(request,'help/help.html',context=my_dict)
