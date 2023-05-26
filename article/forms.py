from django import forms


class CommentsForm(forms.Form):
    title = forms.CharField(max_length=220, widget=forms.TextInput(attrs={
        'placeholder': 'Title'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'col': 5
    }))
