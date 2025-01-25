from django.shortcuts import render
from rest_framework import generics
from . models import *
from . serializer import *

# Create your views here.
class AllCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UpdateDeleteCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AllBlog(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CreateBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class UpdateDeleteBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer