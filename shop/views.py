from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Mahsulot, Toifa
from django.views.generic import ListView, DetailView


def index(request):
    toifa = Toifa.objects.get(pk=1)
    mahsulotlar = Mahsulot.objects.filter(toifasi=toifa)
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', {'toifalar': toifalar, 'mahsulotlar': mahsulotlar})


class IndexView(ListView):
    model = Toifa
    template_name = 'shop/index.html'
    context_object_name = 'toifalar'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['mahsulotlar'] = Mahsulot.objects.all()
        return context


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


class MahsulotListView(ListView):
    model = Mahsulot
    template_name = 'shop/mahsulot_list.html'
    context_object_name = 'tovar_list'


class MahsulotView(DetailView):
    model = Mahsulot
    template_name = 'shop/mahsulot.html'
