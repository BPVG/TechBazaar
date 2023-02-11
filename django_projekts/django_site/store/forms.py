from django import forms
from .models import Listing
from django.contrib.auth.models import User

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['listingname', 'description', 'listingimage', 'price', 'currency']
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']