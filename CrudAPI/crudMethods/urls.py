from django.urls import path
from .views import *

urlpatterns = [
    path('post/', StudentAdd.as_view()),
    path('get/<int:pk>/', StudetnData.as_view()),
]
