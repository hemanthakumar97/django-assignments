from django.shortcuts import render
from .models import School,Student
from django.views.generic import TemplateView,ListView

class SchoolView(ListView):
    model = School
    
class StudentView(ListView):
    model = Student
    template_name = "student_list.html"

