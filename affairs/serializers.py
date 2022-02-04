from .models import student_affairs
from rest_framework import serializers



class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student_affairs
        fields = ['first_name', 'last_name', 'email']