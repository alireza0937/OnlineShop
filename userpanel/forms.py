from django import forms
from account.models import User


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='current password',

    )
    new_password = forms.CharField(
        label='new password'
    )

    repeat_password = forms.CharField(
        label='new password repeat'
    )


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'about_user',
            'address',
            'avatar',

        ]