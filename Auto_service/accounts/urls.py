from django.urls import path
from .views import register, login_view, logout_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
   
    #cdpath('profile/', profile, name='profile'),
]
