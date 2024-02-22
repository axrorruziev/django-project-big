from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('site/', views.index2),
    path('buy/', views.index3, name='buy'),
    path('laptop/', views.index4, name='laptop'),

]