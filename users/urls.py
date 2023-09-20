from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, VerifyEmailView,GenerateAndSendPasswordView

app_name=UsersConfig.name


urlpatterns = [
    path('',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),
    path('verify_email/',VerifyEmailView.as_view(), name='verify_email'),
    path('generate_and_send_password/', GenerateAndSendPasswordView.as_view(), name='generate_and_send_password'),
]