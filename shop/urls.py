from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.testoviy, name='testoviy'),
    path('', views.index, name='index'),
]