from django.shortcuts import render
from form_app import forms
# Create your views here.

def index(request):
    return render(request,'form_app/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("validation success")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    form_dict = {'form':form}
    return render(request,'form_app/form_page.html',form_dict)
