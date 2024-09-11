from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.forms import LoginForm, CustomUserCreationForm # type: ignore


def mechanic_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mechanic_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'mechanic_login.html', {'form': form})

def register_mechanic(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mechanic_login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'mechanic_register.html', {'form': form})

def mechanic_dashboard(request):
    return render(request, 'mechanic_dashboard.html')
