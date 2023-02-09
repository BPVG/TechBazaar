from django.shortcuts import render, redirect
from .models import Listing
from django.views.generic import DetailView
from .forms import ListingForm, RegisterForm
from django.urls import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_detail.html'

def store(request):
    object_list = Listing.objects.filter(statuscompleted=False)
    return render(request, 'store.html', {'object_list': object_list})

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            user_current = request.user
            listing.listinguser = user_current
            listing.save()
            return redirect('store:store')
    else:
        form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('store:store')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

class ListingCreateView(CreateView):
    model = Listing
    fields = ['listingname', 'description', 'listingimage', 'price','currency']
    template_name = 'listing_form.html'
    success_url = reverse_lazy('store')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "invalid username or password"}
            return render(request, 'registration/login.html', context)
        login(request, user)
        return redirect("store:store")
    return render(request, 'registration/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request, 'registration/logout.html', {})
