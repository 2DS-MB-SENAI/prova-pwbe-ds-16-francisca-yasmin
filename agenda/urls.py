from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.read_servicos),
    path('servicos/criar', views.create_servicos),
]