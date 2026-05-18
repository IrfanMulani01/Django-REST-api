from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .serializer import StudentSerializer
from .models import Student


class StudentAdd(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error_messages)
    
class StudetnData(APIView):
    def get(self, request, pk=None):

        if pk is not None:
            student = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)