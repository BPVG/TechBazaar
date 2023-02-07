from django.shortcuts import render, redirect
from .models import Listing
from django.views.generic import DetailView
from .forms import ListingForm
from django.urls import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_detail.html'

def store(request):
    object_list = Listing.objects.filter(statuscompleted = False)
    return render(request, 'store.html', {'object_list': object_list})

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.listinguser = request.user.id
            listing.save()
            return redirect('store')
    else:
        form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

class ListingCreateView(CreateView):
    model = Listing
    fields = ['listingname', 'description', 'listingimage', 'price','currency']
    template_name = 'listing_form.html'
    success_url = reverse_lazy('store')

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return confirm_password