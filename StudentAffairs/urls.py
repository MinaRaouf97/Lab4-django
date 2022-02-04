"""StudentAffairs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from posixpath import basename
from django.contrib import admin
from django.urls import path,include,re_path
from user.views import *
from affairs.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'students',Studentview,basename='student_affairs')

# router.register(r'students/<int:pk>',studentUpdateApiView,basename='student_affairsU')

# router.register(r'students/<int:pk>',studentUpdateApiView,basename='student_affairs')








urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',loginUser),
    path('register',registerUser),
    path('home',home),
    path('addstudent',insertStudent),
    path('allstudents',studentList),
    path('<int:id>',showStudent),
    path('searchStudent',studentList),
    path('logout',mylogout,name='logout'),
    path('genericlist', trackList.as_view(), name='genericlist'),
    path('addstudentForm1',addStudentView),
    path('addstudentForm2',addStudentviewModel),
    
    path('', include(router.urls)),
    path('students/', include('rest_framework.urls', namespace='rest_framework')),
    
    # re_path(r'^students/(?P<pk>[0-9]+)$',studentUpdateApiView, name='update'),
    
    path('students/<int:pk>',studentUpdateApiView, name='update'),


    # path('<pk>/update',UpdateView.as_view())
    
    # path('deletestudent/<studentid>',deleteStudent)

]
