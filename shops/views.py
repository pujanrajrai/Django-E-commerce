from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):

    return render(request,'shops/index.html')

def about(request):
    return HttpResponse('about us')

def contact(request):
    return HttpResponse('contact us')

def tracker(request):
    return HttpResponse('tracking product')

def search(request):
    return HttpResponse('searching ')

def productview(request):
    return HttpResponse('viewing prodect')