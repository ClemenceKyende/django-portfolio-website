# Import Django's forms module to create forms
from django import forms

# Define a ContactForm for handling contact form submissions
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number(Optional)'})
    )
    message = forms.CharField(
        widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Your Message (min. 100 characters)', 'rows': 4}),
        min_length=100
    )
