from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['full_name', 'email', 'your_message']
