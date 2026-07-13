from django.shortcuts import render
from rest_framework import viewsets
from .models import PostModel
from .serializer import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
