from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('room/', views.room, name='room'),

path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('product/', views.product, name='product'),

]