from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *

@api_view(['GET'])
def show(request):
    student = Student.objects.all()

    serializer = StudentSerializer(student, many = True)

    return Response(serializer.data)


@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data)
    