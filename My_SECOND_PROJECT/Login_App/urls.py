from django.urls import path
from . import views

app_name = "Login_App"

urlpatterns = [
    path("",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("login/",views.login_page,name="login"),
    
    ## redirection url is in the settings.py last line
    ## you must give the begining '/' before logout
    ## to match the redirect patterns
    path('/logout',views.user_logout,name="logout")
]
