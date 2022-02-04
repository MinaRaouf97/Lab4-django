from dataclasses import fields
from django import forms
from .models import student_affairs



class addStudentForm(forms.Form):
    first_name=forms.CharField(max_length=10,label='First Name ')
    last_name=forms.CharField(max_length=10 ,label='Last Name ')
    email =forms.EmailField(max_length=40, label='Email ')



class addStudentFormtwo(forms.ModelForm):
    class Meta:
        model=student_affairs
        fields='__all__'