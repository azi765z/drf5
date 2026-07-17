from django.shortcuts import render
from rest_framework import viewsets
from .models import CourseModel
from .serializer import CourseSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer