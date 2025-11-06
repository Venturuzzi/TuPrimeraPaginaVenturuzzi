from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView, about_view

app_name = 'blogpages'

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('create/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('<int:pk>/edit/', PageUpdateView.as_view(), name='page_update'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
    path('about/', about_view, name='about'),
    
]
