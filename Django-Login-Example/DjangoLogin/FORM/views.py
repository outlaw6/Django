from django.shortcuts import render
from FORM import forms
# Create your views here.


def index(request):
    return render(request, 'FORM/index.html')

def form_name_view(request):

    #Create forms

    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            # Do something on the FORM is reqMethod is POST
            # and Form is is_valid
            print("Validatated.")

            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    return render(request, 'FORM/form_page.html', {'form': form})
