from django.shortcuts import render
from django.http import HttpResponse

#from Login.models import Name

from Login.forms import NewUser
def index(request):

    #name_list = Name.objects.order_by('top_name')
    #name_dict = {'name_records': name_list}
    name_dict = {'name_records': 'name'}
    return render(request, 'users/index.html')

def users(request):

    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True) # Save the form
            return index(request)
        else:
            print("Error, form invalid")

    return render(request, 'users/users.html', {'form': form})
