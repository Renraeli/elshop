from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Mahsulot, Toifa


def index(request):
    toifa = Toifa.objects.get(pk=1)
    mahsulotlar = Mahsulot.objects.filter(toifasi=toifa)
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', {'toifalar': toifalar, 'mahsulotlar': mahsulotlar})


def testoviy(request):
    return HttpResponse('Hello LINK')


def category(request, category_id):
    page = request.GET.get('page')
    toifa = Toifa.objects.get(pk=category_id)
    all_mahsulotlar = Mahsulot.objects.filter(toifasi=toifa)
    paginator = Paginator(all_mahsulotlar, 3)
    mahsulotlar = paginator.get_page(page)
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', {'toifalar': toifalar, 'mahsulotlar': mahsulotlar})


