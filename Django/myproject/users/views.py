from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('registration_success')  # Redirect to success page
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def registration_success(request):
    return render(request, 'users/success.html')

def home(request):
    return render(request, 'users/home.html')