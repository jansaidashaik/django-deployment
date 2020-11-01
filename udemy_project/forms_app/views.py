from django.shortcuts import render
from forms_app import forms


# Create your views here.

def index(request):
    return render(request, 'forms_app/index.html')


def form_page_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print("Name : {} ".format(form.cleaned_data['name']))
            print("Email: {}".format(form.cleaned_data['email']))
            print("Text : {}".format(form.cleaned_data["text"]))
    context = {
        'form': form
    }
    return render(request, 'forms_app/form_page.html', context)
