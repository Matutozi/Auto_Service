from django.shortcuts import render

def mechanic_dashboard(request):
    return render(request, 'mechanic_dashboard.html')
