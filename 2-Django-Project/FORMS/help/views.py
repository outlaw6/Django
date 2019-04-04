
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me': "We are in HELP APP"}
    return render(request, 'help/index.html', context=my_dict)
