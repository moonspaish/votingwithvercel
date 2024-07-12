from django.urls import path
from . import views

urlpatterns = [
    path('', views.vote, name='vote'),
    path('success/', views.success, name='success'),
    path('histogram/', views.histogram, name='histogram'),
]
