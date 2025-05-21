from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin-messages/', views.admin_messages, name='admin_messages'),
    path('clear-messages/', views.clear_messages, name='clear_messages'),
    path('technique/<int:pk>/', views.technique_detail, name='technique_detail'),

]