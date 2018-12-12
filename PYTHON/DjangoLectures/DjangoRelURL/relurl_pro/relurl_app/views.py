from django.shortcuts import render
from relurl_app.forms import NameForm
# Create your views here.
def index(request):
    my_dict = {'name':'tracerZZ'}
    return render(request,'relurl_app/index.html',context=my_dict)

def formpage(request):
    form = NameForm()
    if request.method == 'POST':
        form = NameForm(request.POST)
        form.save(commit=True)
    return render(request,'relurl_app/form.html',{'form':form})
