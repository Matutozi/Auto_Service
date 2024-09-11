from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.mechanic_dashboard, name='mechanic_dashboard'),
    path('login/', views.mechanic_login, name='mechanic_login'),
    path("register/", views.register_mechanic, name='mechanic_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
