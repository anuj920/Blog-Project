from django.urls import path
from django.conf.urls import url

from django.contrib.auth import views as auth_views
from accounts.forms import EmailValidationOnForgotPassword

from accounts import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    path('password-done/',views.Password_DoneView.as_view(),name='password_done'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword), name='password_reset'),
]