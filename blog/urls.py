from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articulos/', views.post_list, name='post_list'),
    path('articulos/nuevo/', views.create_post, name='create_post'),
    path('categorias/nueva/', views.create_category, name='create_category'),
    path('profesionales/nuevo/', views.create_author, name='create_author'),
    path('buscar/', views.search, name='search'),
]
