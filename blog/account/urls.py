from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #Profile
    path('profile/<int:id>/', views.get_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('following/', views.following, name='following'),
    path('profile/<int:profile_id>/<int:follow>', views.get_profile_list_follow, name='list_follow')
]