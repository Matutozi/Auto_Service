from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, DriverRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


@login_required
def driver_dashboard(request):
    services = [
        {'name': 'Emergency Service', 'url': 'emergency_service'},
        {'name': 'Custom Service', 'url': 'custom_service'},
        {'name': 'Scheduled Service', 'url': 'scheduled_service'}
    ]
    return render(request, 'driver_dashboard.html', {"services":services})




def driver_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('driver_dashboard')  # Redirect to the driver's dashboard or a success page
    else:
        form = AuthenticationForm()

    return render(request, 'driver_login.html', {'form': form})


def driver_register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        driver_form = DriverRegisterForm(request.POST)
        
        if user_form.is_valid() and driver_form.is_valid():
            user = user_form.save()
            driver = driver_form.save(commit=False)
            driver.user = user
            driver.save()
            login(request, user)
            return redirect('driver_dashboard')
    
    else:
        user_form = UserRegisterForm()
        driver_form = DriverRegisterForm()

    return render(request, 'driver_register.html', {'user_form': user_form, 'driver_form': driver_form})
