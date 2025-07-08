
from django.urls import path
from home.views import (
    HomeView,
    LoginView,
    LogoutView,
    RegisterView,
)

urlpatterns = [
    path('registro/', RegisterView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='index')
]
