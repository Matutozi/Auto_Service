from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('login', views.driver_login, name='driver_login'),
    path('register', views.driver_register, name='driver_register'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout route

]
