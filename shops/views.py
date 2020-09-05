from django.shortcuts import render
from math import ceil

from .models import Products
# Create your views here.
from django.http import HttpResponse
def index(request):
    product= Products.objects.all()
    n=len(product)
    nSlide= n//4+ceil((n/4)-(n//4))
    #allprods=[[product,range(1,nSlide),nSlide],[product,range(1,nSlide),nSlide]]
    prams={'no_of_slide':nSlide,'product':product,'range':range(1,nSlide)}
    #prams={'allprods':allprods}
    return render(request,'shops/index.html',prams)
    

def about(request):
    return render(request,'shops/about.html')

def contact(request):
    return HttpResponse('contact us')

def tracker(request):
    return HttpResponse('tracking product')

def search(request):
    return HttpResponse('searching ')

def productview(request):
    return HttpResponse('viewing prodect')

def checkout(request):
    return HttpResponse('viewing prodect')

