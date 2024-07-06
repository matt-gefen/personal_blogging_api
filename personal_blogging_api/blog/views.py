from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return HttpResponse("Hello world, you're at the blog index.")