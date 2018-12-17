from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from cbv_app import models
# Create your views here.
#normal way
# def index(request):
#     return render(request,"index.html")
#class based view
# class CBview(View):
#     def get(self,request):
#         return HttpResponse("CBV are cool!")
#CBV with template calling
class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs): #**kwargs is use to get any number of dictionary as parameter
        context = super().get_context_data(**kwargs)
        context['injectme']="BASIC INJECTION" #you can use injectme in html path like {{injectme}}
        return context
#ListView
class SchoolListView(ListView):
    print("here")
    context_object_name = "school_context"
    model = models.School #returns school_list as default if context_obj_name is not declared
#DetailView
class SchoolDetailView(DetailView):
    context_object_name = "schools_detail_context"
    model = models.School #returns school as default if context_obj_name is not declared
    template_name = "cbv_app/school_detail1.html" #this will override the search for _details html file lol
#Another List View
def SchoolInfoView(request):
    model_dict = {"school_model" : models.School.objects.all(),
                  "students_model" : models.Student.objects.all()}
    return  render(request,"cbv_app/school_info.html",context=model_dict)

