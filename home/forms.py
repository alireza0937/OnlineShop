from django import forms
from home.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name',
                  'email',
                  'subject',
                  'message']

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email',
                'class': "form-control"
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject',
                'class': "form-control"
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message',
                'row': 20,
                'id': "message",
                'class': "form-control"
            }),

            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': "form-control"
            }),



        }



