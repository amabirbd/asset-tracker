# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.asset_list, name='asset_list'),
    path('add/', views.asset_add, name='asset_add'),
    path('<int:asset_id>/assign/', views.asset_assign, name='asset_assign'),
    path('<int:asset_id>/return/', views.asset_return, name='asset_return'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
