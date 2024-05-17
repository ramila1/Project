from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.login),
    path('', views.custom_user_list, name='custom_user_list'),
    path('<int:pk>/', views.custom_user_detail, name='custom_user_detail'),
  
    
]


