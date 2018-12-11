'Create a Forms.py file inside app'
    'Creating form is similar to creating a model'
        from django import forms
        class FormName(forms.Form):
            name = forms.CharField()
            email = forms.EmailField()
            text = forms.CharField(widget=forms.Textarea)
    'Create a view for this form similar to html page'
        def form_name_view(request):
        form = forms.FormName()#create object for FromName class from forms.py
        if request.method == 'POST':#enters when submit is pressed
            form = forms.FormName(request.POST)
            if form.is_valid():
                print("validation success")
                print(form.cleaned_data['name'])#prints the submitted info in the form
                print(form.cleaned_data['email'])
                print(form.cleaned_data['text'])
        form_dict = {'form':form}
        return render(request,'form_app/form_page.html',form_dict)
    'Add the url for the views'
