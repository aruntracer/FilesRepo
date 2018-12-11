from django import forms
from django.core import validators

#Validation Method3 using custom validations
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name should start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(10)])
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(10)])

#Validation Method1 rarely used
    # def clean_botcatcher(self):
    #     bot_catcher = self.cleaned_data['botcatcher']
    #     if len(bot_catcher) > 0 :
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return bot_catcher

#Validation Method2 using built in validators
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self): #single clean method for entire form, here clean is keyword
        all_clean_data = super().clean()
        email = all_clean_data['email']
        veriy_email = all_clean_data['verify_email']
        if email != veriy_email:
            raise forms.ValidationError("Make sure emails match!")
