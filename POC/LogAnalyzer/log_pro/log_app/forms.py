from django import forms



class AnalyzeLog_Form(forms.Form):
    log_file = forms.FileField()
