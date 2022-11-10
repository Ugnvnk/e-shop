from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import (UserCreationForm as UserCreationFormDjango, SetPasswordForm)
from django import forms
from django.utils.translation import gettext_lazy as _

from main.models import Product

User = get_user_model()


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
    )


class UserCreationForm(UserCreationFormDjango):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'})
    )

    class Meta(UserCreationFormDjango.Meta):
        model = User
        fields = ("username", "email")


class AuthenticationAjaxForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'class': 'form-control'
            }
        ),
    )

class ProductInput(forms.Form):
        model = Product
        fields = ['name', 'category', 'brand', 'photo', 'price']

