from django.shortcuts import render
from django.http import HttpResponse

from Login.models import Name
def index(request):

    name_list = Name.objects.order_by('top_name')
    name_dict = {'name_records': name_list}

    return render(request, 'users/index.html', context=name_dict)
