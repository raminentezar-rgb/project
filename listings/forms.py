from django import forms
from .models import VisitRequest


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class VisitRequestForm(forms.ModelForm):
    class Meta:
        model = VisitRequest
        fields = ['name', 'email', 'preferred_date', 'message']