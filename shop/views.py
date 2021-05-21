from django.http import HttpResponse
from django.shortcuts import render
from .models import Mahsulot, Toifa


def index(request):
    mahsulotlar = Mahsulot.objects.all()
    return render(request, 'shop/index.html', {'mahsulotlar': mahsulotlar})


def testoviy(request):
    return HttpResponse('Hello LINK')
