#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('时代科技福克斯')

def add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=str(int(a)+int(b))
    return HttpResponse(c)

def add2(request,a,b):
    c=str(int(a)+int(b))
    return HttpResponse(c)

def home(request):
    c=u'把发动机奥斯卡房间看书'
    tutorialList=['webpacge','react','bootstrip','yeomen','flux']
    tutorialDict={'name':'王尼玛','age':34,'like':'飞飞'}
    return render(request, 'myapp/home.html',{'d':c,'tlist':tutorialList,'tdict':tutorialDict})
