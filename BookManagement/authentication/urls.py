from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('password-change/', views.UserPasswordChangeView.as_view(),
         name='password_change'),
    path('password_reset/', views.UserPasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
