from itertools import product

from django.shortcuts import render
from rest_framework import viewsets
from .models import CourseModel
from .serializer import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def courses_listview(request):
    courses = CourseModel.objects.all()
    serializer = CourseSerializer(courses,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def courses_create(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({"message": "User Create Error"})

@api_view(['GET'])
def courses_detail(request,pk):
    courses = CourseModel.objects.get(pk=pk)
    serializer = CourseSerializer(courses)
    return Response(serializer.data)

@api_view(['PUT'])
def courses_update(request,pk):
    courses = CourseModel.objects.get(pk=pk)
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'errors'})



@api_view(['DELETE'])
def courses_delete(request,pk):
    courses = CourseModel.objects.get(pk=pk)
    courses.delete()
    return Response({'message': 'courses deleted'})

@api_view(['PATCH'])
def courses_patch(request,pk):
    courses = CourseModel.objects.get(pk=pk)
    serializer = CourseSerializer(courses, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'errors': serializer.errors})