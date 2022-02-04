from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
from .models import affairs_user



def mylogout(request):
    if 'username' in request.session:
         print('yes!')
    request.session['username']=None
    request.session['authuser']=None
    logout(request)
    return render(request, 'user/login.html')

def loginUser(request):
    context={}
    if(request.method=="GET"):
        return render (request,'user/login.html')
    else:
        username=request.POST['userName']
        email=request.POST['email']
        password=request.POST['password']
        try:
            authuser= authenticate(username=username,password=password)
            user= affairs_user.objects.get(name=username,email=email,password=password)
            if(authuser is not None and user is not  None):
                login(request,authuser)
                print("=========================================================")
                print(user.name)
                print(authuser.username)
                request.session['username']=user.name    
                request.session['authuser']=authuser.username
                print("=========================================================")

                return redirect('/allstudents')
            else:
                print("errrrrrrrrrrrrrrrrroooooooooooooooooooooooooorrrrrrrrrrrrrrrrrr  ")

                # return HttpResponseRedirect('/allstudents')
        except affairs_user.DoesNotExist :
            #else print errr statment
            print('not loggined')
            context['errormsg']='incalid cred.'
            return render(request, 'user/login.html', context)
            
        # else:
        #     else print errr statment
        #     print('not loggined')
        #     context['errormsg']='incalid cred.'
        #     return render(request, 'user/login.html', context)

def registerUser(request):
    context={}
    if (request.method=='GET'):
        return render (request,'user/register.html')
    else: 
        affairs_user.objects.create(name=request.POST['name'],password=request.POST['password'],email=request.POST['email'])
        User.objects.create_user(username=request.POST['name'],email=request.POST['email'],password=request.POST['password'],is_staff=True)
        user=affairs_user.objects.all()
        print(user)
        return redirect('/login',{'user':user})



def home(req):
    return render (req,'user/home.html')
