from django.contrib import admin
from django.urls import path
from . import views

app_name = 'comms'

urlpatterns = [
    path('', views.comms_list, name='list'),
    path('<slug:slug>', views.comm_page, name='page'),
]
