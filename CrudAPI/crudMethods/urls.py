from django.urls import path
from .views import *

urlpatterns = [
    path('post/', StudentAdd.as_view()),
    path('get/<int:pk>/', StudetnData.as_view()),
    path('get/', ListStud.as_view()),
    path('put/<int:pk>/', PutStud.as_view()),
    path('patch/<int:pk>/', PatchStud.as_view()),
    path('delete/<int:pk>/', DeleteStud.as_view()),
]
