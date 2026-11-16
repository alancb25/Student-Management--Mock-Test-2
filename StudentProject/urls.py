"""
URL configuration for StudentProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from studApp.views import AllStudentListView, DeleteStudentView, ProfileCreateView, UserCreateView, UserListView,ProfileRetrieveUpdateDestroyView

from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usercreate',UserCreateView.as_view(),name="user_create"),
    path('profilecreate',ProfileCreateView.as_view(),name="profile_create"),

    
    
    path('userlist',UserListView.as_view(),name="user_list"),
    path('studentlist',AllStudentListView.as_view(),name="allprofile_list"),
    path('profilelist/<int:pk>',ProfileRetrieveUpdateDestroyView.as_view(),name="student-profile"),


    path('studentupdate/<int:pk>',ProfileRetrieveUpdateDestroyView.as_view(),name="update_all"),
    path('studentdelete/<int:pk>',DeleteStudentView.as_view(),name="student-delete"),

    path('token',auth_view.obtain_auth_token), 


]
    