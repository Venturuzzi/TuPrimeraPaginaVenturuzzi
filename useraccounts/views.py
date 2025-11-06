from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignupForm, ProfileForm
from .models import Profile


# 🔹 Registro de usuario nuevo
def signup_view(request):
    """
    Permite a un nuevo usuario registrarse y crea su perfil asociado.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # Evita duplicados: crea el perfil solo si no existe
            Profile.objects.get_or_create(user=user)

            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('blogpages:page_list')
    else:
        form = SignupForm()

    return render(request, 'useraccounts/signup.html', {'form': form})


# 🔹 Inicio de sesión
def login_view(request):
    """
    Inicia sesión si las credenciales son correctas.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('blogpages:page_list')
        else:
            messages.error(request, 'Credenciales incorrectas.')
    return render(request, 'useraccounts/login.html')


# 🔹 Cierre de sesión
def logout_view(request):
    """
    Cierra la sesión del usuario actual.
    """
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('useraccounts:login')


# 🔹 Vista del perfil
@login_required
def profile_view(request):
    """
    Muestra los datos personales y del perfil extendido del usuario.
    """
    return render(request, 'useraccounts/profile.html', {
        'profile': request.user.profile,
        'user': request.user,
    })


# 🔹 Edición del perfil
@login_required
def profile_edit_view(request):
    """
    Permite al usuario editar su información y la del perfil asociado.
    """
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            # Actualiza también los datos del usuario
            user.first_name = form.cleaned_data.get('first_name', user.first_name)
            user.last_name = form.cleaned_data.get('last_name', user.last_name)
            user.email = form.cleaned_data.get('email', user.email)
            user.save()

            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('useraccounts:profile')
    else:
        form = ProfileForm(instance=profile)
        form.fields['first_name'].initial = user.first_name
        form.fields['last_name'].initial = user.last_name
        form.fields['email'].initial = user.email

    return render(request, 'useraccounts/profile_edit.html', {'form': form})


# 🔹 Cambio de contraseña
class CustomPasswordChangeView(PasswordChangeView):
    """
    Vista para permitir el cambio de contraseña del usuario autenticado.
    """
    template_name = 'useraccounts/change_password.html'
    success_url = reverse_lazy('useraccounts:profile')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada correctamente.')
        return super().form_valid(form)
