from django.urls import path
from .views import ShowAPIView

urlpatterns = [
    path('', ShowAPIView.as_view()),
]