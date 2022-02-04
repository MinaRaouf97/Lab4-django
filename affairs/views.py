from cmath import e
import imp
from multiprocessing import context
from pyexpat import model
from django.shortcuts import render , redirect
from .models import student_affairs ,Intake,track
from django.views.generic import ListView
from .forms import addStudentForm ,addStudentFormtwo
from django.http import HttpResponseRedirect


from rest_framework import viewsets,permissions

from .serializers import StudentSerializer 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','PUT', 'PATCH','DELETE'])
def studentUpdateApiView(request,pk):
    try:
        student=student_affairs.objects.get(id=pk)
    except student_affairs.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
     
     ## get student data 
        
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        print(serializer)
        return Response(serializer.data)
    
    ## insert student data 
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    ##update student data
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student,data=request.data,partial=True)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

        ## delete student data 
    elif request.method == 'DELETE':
       
        

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Studentview(viewsets.ModelViewSet):
    queryset = student_affairs.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated,permissions.IsAuthenticatedOrReadOnly]
    
    

#### FORMS.FORM IMPLMENTAION
def addStudentView(request):
    
    if (request.method=='GET'):
        form = addStudentForm()
        return render(request,'affairs/addStudentForm1.html',{'form':form})

    else:
        form = addStudentForm(request.POST)
        if form.is_valid() :
            try:
                first_name= form.cleaned_data.get('first_name')
                last_name= form.cleaned_data.get('last_name')
                email= form.cleaned_data.get('email')
                student_affairs.objects.create(first_name=first_name,last_name=last_name,email=email)
                form = addStudentForm()

                return render(request,'affairs/addStudentForm1.html',{'form':form})


            except e:
                print(e)
    
    
def addStudentviewModel(request):
        if (request.method=='GET'):
            form = addStudentForm()
            return render(request,'affairs/addStudentForm2.html',{'form':form})
        else:
            form = addStudentFormtwo(request.POST)
            if form.is_valid():
                form.save()
                form = addStudentForm()
                return render(request,'affairs/addStudentForm2.html',{'form':form})


    
    


            
            
########### list with GENERIC VIEW ###########

class trackList(ListView):
    model=track
# Create your views here.



def insertStudent(request):
    if(request.method=='GET'):
        return render(request,'affairs/insertStudent.html')
    else:
        try:
            student_affairs.objects.create(first_name=request.POST['firstName'],last_name=request.POST['lastName'],email=request.POST['email'])
            # user=student_affairs.objects.all()
            # print(user)
            return render(request,'affairs/insertStudent.html')

            
        except e:
            print(e)
    
    
    
def allStudents(request):
    context={}
    if (request.method=='GET'):
        context['students']=student_affairs.objects.all()
        return render(request,'affairs/allStudent.html',context)
    elif(request.method=='POST' and 'searchStudent' in request.POST):
        context['students']=student_affairs.objects.get(first_name=request.POST['firstName'])
        return redirect(request,'/searchStudent',context)



def deleteStudent(request):
    print('del STudent')
    if(request.method=='POST' and 'deleteStudent' in request.POST):
        print(request.POST['studentid'])
       
        student=student_affairs.objects.get(id=request.POST['studentid'])
        student.delete()
        
def studentList(request):
    context={}
    if (request.method=='GET'):
        context['students']=student_affairs.objects.all()
        return render(request,'affairs/allStudent.html',context)
    elif(request.method=='POST' and 'deleteStudent' in request.POST):
        student=student_affairs.objects.get(id=request.POST['studentid'])
        student.delete()
        return redirect('/allstudents')
    elif(request.method=='POST' and 'searchStudent' in request.POST):
        context['students']=student_affairs.objects.filter(first_name__contains=request.POST['firstNameSearch'])
        return render(request,'affairs/searchStudent.html',context)


def showStudent(request,id):
        context={}
        if(request.method=='GET'):
            context["studentData"] = student_affairs.objects.get(id=id)
            return render(request, "affairs/updateStudent.html", context)
        else:
            student=student_affairs.objects.get(id=request.POST['studentid'])
            student.first_name=request.POST['firstName']
            student.last_name=request.POST['lastName']
            student.email=request.POST['email']
            student.save()
            return redirect('/allstudents')


            



# class UpdateView(UpdateView):
#     # specify the model you want to use
#     model = student_affairs
  
#     # specify the fields
#     fields = [
#         "first_name",
#         "last_name",
#         "email"
#     ]
#     template_name = 'affairs/updateStudent.html' # templete for updating

#     # can specify success url
#     # url to redirect after successfully
#     # updating details
#     success_url ="/allstudents"
        

        
        
     
    
