from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.forms import LoginForm, CustomUserCreationForm # type: ignore
from .forms import MechanicRegister, UserRegisterForm

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
        user_form = UserRegisterForm(request.POST)
        mechanic_form = MechanicRegister(request.POST)
        
        if user_form.is_valid() and mechanic_form.is_valid():
            user = user_form.save()
            user_profile = mechanic_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            
            login(request, user)  # Automatically log in the user
            return redirect('mechanic_dashboard')  # Redirect to a relevant page

    else:
        user_form = UserRegisterForm()
        mechanic_form = MechanicRegister()
    
    return render(request, 'mechanic_register.html', {
        'user_form': user_form,
        'mechanic_form': mechanic_form
    })
def mechanic_dashboard(request):
    return render(request, 'mechanic_dashboard.html')
