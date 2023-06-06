from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(label='E-Mail Address')
    password = forms.CharField(label='password')
    confirm_password = forms.CharField(label='confirm password')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError("passwords are not same")


class LoginForm(forms.Form):
    email = forms.EmailField(label='E-Mail Address')
    password = forms.CharField(label='password')


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()


class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(max_length=100)
    repeat_new_password = forms.CharField(max_length=100)
