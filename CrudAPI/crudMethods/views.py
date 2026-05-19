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
    
class ListStud(APIView):
    def get(self, request):
        stud = Student.objects.all()
        serializer = StudentSerializer(stud, many=True)
        return Response(serializer.data)


# class PutStud(APIView):
#     def put(self, request, pk):
#         stud = get_object_or_404(Student, id=pk)
#         serializer = StudentSerializer(stud, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Student Updated",
#                 "data": serializer.data})
#         return Response(serializer.errors)


# class PatchStud(APIView):
#     def patch(self, request, pk):
#         stud = get_object_or_404(Student, id=pk)
#         serializer = StudentSerializer(stud, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response({"Message": "update succesfully", "data":serializer.data})
#         return Response(serializer.errors)

    
# class DeleteStud(APIView):
#     def delete(self, request, pk):
#         stud = get_object_or_404(Student, id=pk)
#         stud.delete()
#         return Response({"Message": "Record delete successfully"})
    