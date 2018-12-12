from django import forms
from relurl_app.models import employee

class NameForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
