from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views import View
from home.forms import LoginForm, RegisterForm
from django.utils.translation import activate, get_language, deactivate

# Vista para página principal
class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

# Cierre de sesión
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

# Registro de nuevos usuarios
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/registro.html', {"form" : form})

    def post(self, request):
        form = RegisterForm(request.POST)        
        if form.is_valid():
            # Crear usuario
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )

            # Enviar correo de bienvenida
            subject = "Registro exitoso"
            message = render_to_string('mails/welcome.html', {'email': user.email})
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email]
            )
            email.content_subtype = 'html'
            email.send(fail_silently=False)

            # Confirmar al usuario
            messages.success(request, "Usuario registrado correctamente")

        return render(request, 'accounts/registro.html', {"form": form})

# Login de usuarios existentes
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Has iniciado sesion")
                return redirect("index")
            else:
                messages.error(request, "El usuario o contraseña no coinciden")

        return render(request, "accounts/login.html", {'form': form})
