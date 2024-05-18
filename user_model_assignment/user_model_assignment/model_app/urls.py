from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.UserLogin.login,name='login'),
    path('', views.UserList.custom_user_list, name='user_list'),
    path('<int:pk>/', views.UserDetail.custom_user_detail, name='user_detail'),
    path('<int:pk>/restore/', views.Restore_User.restore_user, name='restore_user'),
  
    
]
