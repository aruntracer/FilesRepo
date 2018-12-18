from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = "log_app\\index.html"

class AzlogView(TemplateView):
    template_name = "log_app\\analyze_log.html"

class AzsiteView(TemplateView):
    template_name = "log_app\\analyze_site.html"
