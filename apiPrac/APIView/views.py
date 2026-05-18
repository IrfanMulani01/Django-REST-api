from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

class ShowAPIView(APIView):

    def get(self, request):
        data = {
            'message': 'Hello API'
        }
        return Response(data)