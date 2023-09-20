from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from catalog.forms import StyleFormMixin
from users.models import User


class UserForm(StyleFormMixin,UserCreationForm):

    class Meta:
        model=User
        fields=('email','password1','password2')

#class UserProfileForm(UserChangeForm):
#    class Meta:
#        model = User
#        fields = ('email', 'first_name', 'last_name', 'phone_number', 'country', 'avatar')


class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))