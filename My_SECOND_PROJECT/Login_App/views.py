from django.shortcuts import render
from .models import User,UserInfo
from .forms import UserForm,UserInfoForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
def index(request):
    if request.user.is_authenticated:
        current_user = request.user 
        print(current_user)
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)

        ## you want any relational data
        ## use double underscore from one table to another table
        ## of relation
        ## like this currentcolumn__related_column
        ## user -> is a column in the UserInfo column
        ## pk   -> is a columnin the user table   
        ## thats how django make relationship
        ## it gets the pk then find the user then search
        ## UserInfo based on that user

        user_more_info  = UserInfo.objects.get(user__pk=user_id)
        return render(request,'Login_App/index.html',{'user_basic_info':user_basic_info,'user_more_info':user_more_info})
    else:
        return render(request,'Login_App/index.html')




def register(request):
    ## we will combine this two form
    ## togather
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)
        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            ## this set function encrypt
            ## insted of plain save
            user.set_password(user.password)
            user.save()


            user_info = user_info_form.save(commit=False)
            user_info.user = user
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            user_info.save()
            registered = True

    else:

        user_form = UserForm()
        user_info_form = UserInfoForm()
    return render(request,'Login_App/register.html',{'user_form':user_form,'user_info_form':user_info_form,'registered':registered})

def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('Login_App:index'))
    return render(request,'Login_App/login.html',{'login_form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_App:index'))