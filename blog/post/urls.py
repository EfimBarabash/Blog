from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('liked/', views.liked, name='liked'),
    path('by_subscription/', views.by_subscription, name='by_subscription'),
    path('get_post/<int:pk>', views.get_post, name='get_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('del_post/<int:pk>/', views.del_post, name='del_post'),
    path('updated_post/<int:pk>/', views.updated_post, name='updated_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('like/', views.like_to_post, name='like')
]