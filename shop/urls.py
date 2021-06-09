from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views import View
from django.views.generic import TemplateView
from shop.views import MahsulotListView, MahsulotView, IndexView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mahsulot/<int:pk>/', MahsulotView.as_view()),
    path('mahsulotlar/', MahsulotListView.as_view()),
    path('test/', views.testoviy, name='testoviy'),
    path('category/<int:category_id>/', views.category, name='category'),
    # path('', views.index, name='index'),
    path('temp/', TemplateView.as_view(template_name='shop/temp.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
