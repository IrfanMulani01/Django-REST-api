from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.context_processors import request
from rest_framework import status

@api_view(['GET'])
def get_method(request):
    students = [
        {'id': 1,
        'name': 'suraj',},
        {
            'id':2,
            'name':'irfan',
        }
    ]

    return Response(students)

@api_view(['POST'])
def post_method(request):

    data = request.data

    return Response({
        'massege': 'student add successully',
        'data': data,
    })

@api_view(['PUT'])
def put_method(request):

    data = request.data

    return Response({
        'message': 'Data will updated',
        'data': data
    })

@api_view(['PATCH'])
def patch_method(request):
    data = request.data

    return Response({
        'message': 'update data successfully',
        'data': data

    })

@api_view(['DELETE'])
def delete_method(request):
    data = request.data

    return Response({
        'message': 'delete data successfully',
        'data': data
    })