from django import forms
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
    password_confirm = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetir contraseña'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

   
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data



class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField(label="Correo electrónico", required=False)
    avatar = forms.ImageField(label="Avatar", required=False)
    bio = forms.CharField(
        label="Biografía",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )
    link = forms.URLField(label="Link", required=False)
    birthday = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'birthday']
