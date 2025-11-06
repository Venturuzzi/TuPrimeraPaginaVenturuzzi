from django.urls import path
from . import views

app_name = 'messagesapp'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent, name='sent'),
    path('compose/', views.compose, name='compose'),
    path('thread/<int:pk>/', views.thread, name='thread'),
]
