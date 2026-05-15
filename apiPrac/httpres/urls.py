from django.urls import path
from .views import *

urlpatterns = [
    path('', get_method),
    path('add/', post_method),
    path('update/', put_method),
    path('patchUpdate/', patch_method),
    path('delete/', delete_method),
]
