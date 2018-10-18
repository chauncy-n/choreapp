from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    path('chores/', views.chores_index, name='chores_index'),
    path('chores/<int:chore_id>', views.chores_detail, name='chores_detail'),  
    path('chores/create/', views.ChoreCreate.as_view(), name='chores_create'),
    path('chores/<int:pk>/update/', views.ChoreUpdate.as_view(), name='chores_update'),
    path('chores/<int:pk>/delete/', views.ChoreDelete.as_view(), name='chores_delete'),
    path('children/', views.children_index, name='children_index'),
    path('children/<int:child_id>', views.children_detail, name='children_detail'),
    path('children/create/', views.ChildCreate.as_view(), name='children_create'),
    path('children/<int:pk>/update/', views.ChildUpdate.as_view(), name='children_update'),
    path('children/<int:pk>/delete/', views.ChildDelete.as_view(), name='children_delete'),
    path('rewards/', views.rewards_index, name='rewards_index'),
    path('rewards/<int:reward_id>', views.rewards_detail, name='rewards_detail'),  
    path('rewards/create/', views.RewardCreate.as_view(), name='rewards_create'),
    path('rewards/<int:pk>/update/', views.RewardUpdate.as_view(), name='rewards_update'),
    path('rewards/<int:pk>/delete/', views.RewardDelete.as_view(), name='rewards_delete'),
]
