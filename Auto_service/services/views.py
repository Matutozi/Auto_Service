from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ServiceRequest
from .forms import ServiceRequestForm

def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequest(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Service Request Valid")
        else:
            return HttpResponse("Error during service request")
    else:
        form = ServiceRequestForm()
    return render(request, 'create_service_request.html', {'form': form})
