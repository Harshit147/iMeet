from django.contrib import admin
from django.urls import path
from .views import index,room
app_name='iChat'
urlpatterns = [

    path('', index, name='index'),
    path('', room, name='room'),
]
