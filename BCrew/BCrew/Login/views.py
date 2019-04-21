from django.shortcuts import render
from Login.forms import UserProfileInfoForm, UserForm

from django.contrib.auth import authenticte, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Login/index.html')
    
@login_required
def special(request):
    return HttpResponse("Logged in!")

@login_required
def user_logoout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) # hashing password
            user.save() # saves in db

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True # if all good change flag
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'Login/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def ulogin(request):

    if request.method == "POST":

        username = request.POST.get('usernmae') # gets username method
        password = request.POST.get('password')

        user = authenticte(username=username, password=password) # Djaggo authenticates the username

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Not good, someone tried to login  && Failed")
            return HttpResponse("Invalid Credentials")

    else:
        return render(request, 'Login/login.html', {})
