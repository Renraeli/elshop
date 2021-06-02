from django.http import HttpResponse
from django.shortcuts import render
from .models import Mahsulot, Toifa


def index(request):
    toifa = Toifa.objects.get(pk=1)
    mahsulotlar = Mahsulot.objects.filter(toifasi=toifa)
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', {'toifalar': toifalar, 'mahsulotlar': mahsulotlar})


def testoviy(request):
    return HttpResponse('Hello LINK')
