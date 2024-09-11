from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.driver_dashboard, name='driver_dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout route

]
