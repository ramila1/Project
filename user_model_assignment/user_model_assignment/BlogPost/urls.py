from django.urls import path,include
from BlogPost import views


urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),  
    # path('all-users/', views.all_users, name='all_users'),
    path('user-blogs/<int:user_id>/', views.user_blogs, name='user_blogs'),
#     path('all-blogs/', views.all_blogs, name='all_blogs'),

]

