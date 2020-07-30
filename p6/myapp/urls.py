from django.contrib import admin
from django.urls import path
from myapp import views
app_name='myapp'

urlpatterns = [
    path('register/', views.register, name='register')
]
