from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignupForm, ProfileForm
from .models import Profile


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('blogpages:page_list')
    else:
        form = SignupForm()
    return render(request, 'useraccounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('blogpages:page_list')
        else:
            return render(request, 'useraccounts/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'useraccounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('useraccounts:login')


@login_required
def profile_view(request):
    return render(request, 'useraccounts/profile.html', {'profile': request.user.profile})


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('useraccounts:profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'useraccounts/profile_edit.html', {'form': form})
