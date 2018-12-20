from django.shortcuts import render
from log_app.forms import AnalyzeLog_Form
from django.views.generic import TemplateView
# Create your views here.

def AzlogView(request):
    form = AnalyzeLog_Form()
    if request.method == 'POST':
        form = AnalyzeLog_Form(request.POST)
        print("validation success1")
        if form.is_valid():
            print("validation success2")
            print(form.cleaned_data['log_file'])
    form_dict = {'form': form}
    return render(request, 'log_app/analyze_log.html', form_dict)


class IndexView(TemplateView):
    template_name = "log_app/index.html"

# class AzlogView(TemplateView):
#     template_name = "log_app/analyze_log.html"

class AzsiteView(TemplateView):
    template_name = "log_app/analyze_site.html"
