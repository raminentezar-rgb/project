from django import forms


class SignatureForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    title = forms.CharField(
        label='Title',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label='Phone',
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    website = forms.URLField(
        label='Website',
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        label='Profile Image',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )