from rest_framework import serializers
from .models import *

class StudentModelSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'

        # def validateAge(self):