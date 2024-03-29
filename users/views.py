from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView,View

from users.forms import UserForm, PasswordResetForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:verify_email')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user=form.save()
        verification_token = get_random_string(length=15)
        #form.instance.verification_token = verification_token
        send_mail(
            subject='Поздравляем с регестрацией',
            message=f'Ваш код подтверждения {verification_token}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)

class VerifyEmailView(View):
    template_name = 'users/verify_email.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        verification_code = request.POST.get('verification_code')
        User = get_user_model()
        try:
            user = User.objects.get(verification_token=verification_code)
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return redirect('users:confirmation_success')
        except User.DoesNotExist:
            pass
        return redirect('users:login')

class GenerateAndSendPasswordView(View):
    template_name = 'users/generate_and_send_password.html'
    form = PasswordResetForm()

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        self.form = PasswordResetForm(request.POST)
        if self.form.is_valid():
            email = self.form.cleaned_data['email']
            User = get_user_model()

            try:
                user = User.objects.get(email=email)

                new_password = get_random_string(length=15)
                user.set_password(new_password)
                user.save()

                send_mail(
                subject = 'Ваш новый пароль для входа',
                message = f'Ваш новый пароль: {new_password}',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [email],
                )

                return render(request, 'users/login.html', {'email': email})
            except User.DoesNotExist:
                pass

        return render(request, 'users/password_reset_error.html')
