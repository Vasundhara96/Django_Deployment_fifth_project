from django.shortcuts import render
from usermodel_app.models import UserProfInfo
from usermodel_app.forms import UserForm,UserProfInfoForm

#Built-in django tools for LOGIN module
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'usermodel_app/index.html')

@login_required #--to logout the current user - built in decorator
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if (request.method == 'POST'):
        user_form = UserForm(request.POST)
        profile_form = UserProfInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #HASH applies
            user.save() #Saving after hashing

            profile = profile_form.save(commit=False)
            profile.user = user #OneToOneField to avoid override of the users
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfInfoForm()

    return render(request,'usermodel_app/register.html',
    {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT not ACTIVE")
        else:
            print("Authentication failed, Invalid Username / Password")
            print("Username: " +username+ "Password: " +password)
    else:
        return render(request,'usermodel_app/login.html')
