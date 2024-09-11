from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def driver_dashboard(request):
    services = [
        {'name': 'Emergency Service', 'url': 'emergency_service'},
        {'name': 'Custom Service', 'url': 'custom_service'},
        {'name': 'Scheduled Service', 'url': 'scheduled_service'}
    ]
    return render(request, 'driver_dashboard.html', {"services":services})