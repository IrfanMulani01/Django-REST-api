from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

@api_view(['GET'])
def studentView(request):
    students = Student.objects.all()

    serializer = StudentModelSerializer(students, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def addStudent(request):
    serializer = StudentModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error_messages)
