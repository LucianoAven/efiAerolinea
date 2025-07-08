from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Formulario de registro personalizado
class RegisterForm(forms.Form):
    username = forms.CharField(
        label = "Nombre de Usuario",
        max_length = 150,
        widget= forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label = "Contraseña",
        max_length = 150,
        widget= forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label = "Repetir la contraseña",
        max_length = 150,
        widget= forms.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label = "Correo Electronico",
        widget= forms.EmailInput(attrs={'class': 'form-control'})
    )

    # Validación para evitar usuarios repetidos
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este usuario ya fue utilizado")
        return username

    # Validación para evitar correos duplicados
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email ya fue utilizado")
        return email

    # Validación cruzada de contraseñas
    def clean(self):
        cleanned_data = super().clean()
        pass1 = cleanned_data.get("password1")
        pass2 = cleanned_data.get("password2")

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError("Las contraseñas no coinciden")


# Formulario de login simple
class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Nombre de usuario",
        max_length= 150,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label = "Contraseña",
        widget = forms.PasswordInput(attrs={'class': 'form-control'})
    )
