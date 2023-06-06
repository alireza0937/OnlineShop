from django import forms

options = (
    ('1', 'Cash on Delivery'),
    ('2', 'Direct Bank Transfer'),
    ('3', 'PayPal'),
)


class PaymentForm(forms.Form):
    choices = forms.ChoiceField(choices=options,
                                label='Choose Your Payment Way',
                                widget=forms.RadioSelect,
                                error_messages={
                                    'invalid': 'You Should Accept Our Terms And Conditions.'
                                },
                                required=True,
                                )
    terms_and_condition = forms.BooleanField(required=True, error_messages={
        'required': 'You Should Accept Our Terms And Conditions.'
    })
