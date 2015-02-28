from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def test01(request):
    return render(request, 'test01.html')

def test02(request):
    return render(request, 'test02.html')

    
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def ajax_list(request):
    a = range(100)
    return JsonResponse(a)
 
def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)
