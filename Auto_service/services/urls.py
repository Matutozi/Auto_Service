from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_service_request, name='create_service'),
    #not created yet
    path('emergency/', views.emergency_services, name='emergency_service'),
    path('custom/', views.custom_services, name='custom_service'),
    path('scheduled/', views.scheduled_service, name='scheduled_service'),
    path('services', views.all_services, name='all Services'),
    # Add more URL patterns here
]
