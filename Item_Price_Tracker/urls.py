"""Item_Price_Tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import register
from django.contrib.auth.views import LoginView,LogoutView
from main_app.views import search,index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# extra
# from Item_Price_Tracker.users.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name = "index"),
    # if register comes in the path name than we have to call the register function
    path('search/',search,name = 'search'),
    path('register/',register,name = 'register-view'),
    path('login/',LoginView.as_view(template_name="users/login.html"),name = "login"),
    path('logout/',LogoutView.as_view(template_name="users/logout.html"),name  = "logout"),

]
