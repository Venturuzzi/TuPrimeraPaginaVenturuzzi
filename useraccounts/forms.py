from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField(label="Correo electrónico", required=False)
    avatar = forms.ImageField(label="Avatar", required=False)
    bio = forms.CharField(label="Biografía", widget=forms.Textarea(attrs={'rows': 3}), required=False)
    link = forms.URLField(label="Link", required=False)
    birthday = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'birthday']
