from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from .models import ServiceRequest
from .forms import ServiceRequestForm

def all_services(request):
     return render(request, "base.html")

def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Service Request Valid")
        else:
            return HttpResponse("Error during service request")
    else:
        form = ServiceRequestForm()
    return render(request, 'create_service_.html', {'form': form})


def scheduled_service(request):
        return render(request, 'emergency_service.html')


def emergency_services(request):
    return render(request, "emergency_service.html")

def custom_services(request):
    return render(request, "custom_service.html")


def service_list(request):
     return render(request, "list_services.html")
