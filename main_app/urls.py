from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chores/', views.chores_index, name='chores_index'),
    path('chores/<int:chore_id>', views.chores_detail, name='chores_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    path('chores/create/', views.ChoreCreate.as_view(), name='chores_create'),
    path('chores/<int:pk>/update/', views.ChoreUpdate.as_view(), name='chores_update'),
    path('chores/<int:pk>/delete/', views.ChoreDelete.as_view(), name='chores_delete'),
    path('children/', views.children_index, name='chores_index'),
    path('children/create/', views.ChildCreate.as_view(), name='children_create'),
    path('children/<int:pk>/update/', views.ChildUpdate.as_view(), name='children_update'),
    path('children/<int:pk>/delete/', views.ChildDelete.as_view(), name='children_delete'),
]

