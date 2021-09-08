from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('del_post/<int:pk>/', views.del_post, name='del_post'),
    path('updated_post/<int:pk>/', views.updated_post, name='updated_post')
]