from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Artículos
    path('articulos/', views.post_list, name='post_list'),
    path('articulos/nuevo/', views.create_post, name='create_post'),

    # Categoría / Profesional
    path('categorias/nueva/', views.create_category, name='create_category'),
    path('profesionales/nuevo/', views.create_author, name='create_author'),

    # Búsqueda
    path('buscar/', views.search, name='search'),

    # Documentos/Recursos
    path('documentos/', views.resource_list, name='resource_list'),
    path('documentos/nuevo/', views.create_resource, name='create_resource'),
]
