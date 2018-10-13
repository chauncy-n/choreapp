from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chores/', views.chores_index, name='choress_index'),
]