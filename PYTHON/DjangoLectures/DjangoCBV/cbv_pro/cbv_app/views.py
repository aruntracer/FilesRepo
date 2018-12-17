from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
# Create your views here.
# def index(request):
#     return render(request,"index.html")

# class CBView(View):
#     def get(self,request):
#         return render(request, "index.html")


class IndexView(TemplateView):
    template_name =  'index.html'

    def get_context_data(self, **kwargs):#what is **kwargs? key ward arguments it takes a dictionary as argument, *args takes any number of values as argument
        context = super().get_context_data(**kwargs)
        context['injectme']='Basic Injection' #this one will be sent to index.html's injectme template tag
        return context

class SchoolListView(ListView):
    context_object_name = 'school'
    model = models.School #here it returns a list with name school_list, we can use this in html using {% school_list %} if we don't give context_object_name else it will take schools

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv_app/school_detail.html'
