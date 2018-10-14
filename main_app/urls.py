from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chores/', views.chores_index, name='chores_index'),
    path('chores/<int:chore_id>', views.chores_detail, name='chores_detail'),
]

