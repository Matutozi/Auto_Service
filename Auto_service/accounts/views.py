from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm, AddressForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        address_form = AddressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save()
            address = address_form.save(commit=False)
            address.custom_user = user.customuser
            address.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            if user.groups.filter(name='Drivers').exists():
                return redirect('driver_dashboard')
            elif user.groups.filter(name='Mechanics').exists():
                return redirect('mechanic_dashboard')
    else:
        user_form = CustomUserCreationForm()
        address_form = AddressForm()

    return render(request, 'register.html', {'user_form': user_form, 'address_form': address_form})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    next_url = request.GET.get('next', 'home_landing')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name='Drivers').exists():
                    return redirect('driver_dashboard')
                elif user.groups.filter(name='Mechanics').exists():
                    return redirect('mechanic_dashboard')
                else:
                    return redirect('home_landing')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home_Landing')

