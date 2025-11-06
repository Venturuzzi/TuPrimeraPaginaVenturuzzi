from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignupForm, ProfileForm
from .models import Profile


# 🔹 Registro de nuevos usuarios
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Crear perfil vacío asociado
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('blogpages:page_list')
    else:
        form = SignupForm()
    return render(request, 'useraccounts/signup.html', {'form': form})


# 🔹 Inicio de sesión
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


# 🔹 Cierre de sesión
def logout_view(request):
    logout(request)
    return redirect('useraccounts:login')


# 🔹 Vista del perfil
@login_required
def profile_view(request):
    """
    Muestra todos los datos del usuario y su perfil extendido.
    """
    return render(request, 'useraccounts/profile.html', {
        'profile': request.user.profile
    })


# 🔹 Edición del perfil
@login_required
def profile_edit_view(request):
    """
    Permite editar los datos del usuario y su perfil.
    """
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.email = request.POST.get('email', user.email)
            user.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('useraccounts:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'useraccounts/profile_edit.html', {'form': form})


# 🔹 Cambio de contraseña
class CustomPasswordChangeView(PasswordChangeView):
    """
    Vista para cambiar la contraseña del usuario.
    """
    template_name = 'useraccounts/change_password.html'
    success_url = reverse_lazy('useraccounts:profile')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada correctamente.')
        return super().form_valid(form)
