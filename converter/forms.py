from django import forms

class ConversionForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    from_currency = forms.ChoiceField(
        choices=[
            ('USD', 'USD'),
            ('EUR', 'EUR'),
            ('GBP', 'GBP'),
            ('INR', 'INR'),
            ('SAR', 'SAR'),
            ('KWD', 'KWD'),
            ('TRY', 'TRY'),
            ('AED', 'AED'),
            ('AFN', 'AFN'),
            ('ALL', 'ALL'),
            ('AMD', 'AMD'),
            ('ANG', 'ANG'),
            ('IDR', 'IDR'),
            ('IRR', 'IRR'),
            # Add more currencies as needed
        ],
        label='From Currency',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    to_currency = forms.ChoiceField(
        choices=[
            ('INR', 'INR'),
            ('USD', 'USD'),
            ('EUR', 'EUR'),
            ('GBP', 'GBP'),
            ('SAR', 'SAR'),
            ('KWD', 'KWD'),
            ('TRY', 'TRY'),
            ('AED', 'AED'),
            ('AFN', 'AFN'),
            ('ALL', 'ALL'),
            ('AMD', 'AMD'),
            ('ANG', 'ANG'),
            ('IDR', 'IDR'),
            ('IRR', 'IRR'),
            
            # Add more currencies as needed
        ],
        label='To Currency',
        widget=forms.Select(attrs={'class': 'form-control'})
    )