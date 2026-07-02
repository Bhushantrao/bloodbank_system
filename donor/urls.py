from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_page'),
    path('', views.home, name='home'),
    path('add/', views.add_donor, name='add_donor'),
    path('view/', views.view_donors, name='view_donors'),
    path('search/', views.search_donor, name='search_donor'),
    path('request/', views.request_blood, name='request_blood'),
]