from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #my_dict = {'insert_me': "iM FROM views.py"}
    return render(request, 'index.html')
