from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'authentication/registration.html'
    success_url = reverse_lazy('authentication:login')


class UserLoginView(LoginView):
    template_name = 'authentication/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('core:book_list')


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'authentication/change_password.html'
    success_url = reverse_lazy('core:book_list')


class UserPasswordResetView(PasswordResetView):
    template_name = 'authentication/password_reset_request.html'
    email_template_name = 'authentication/password_reset_emai.html'
    success_url = reverse_lazy('core:book_list')


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('authentication:login')
