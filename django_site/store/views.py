from django.shortcuts import render, redirect, get_object_or_404
from .models import Listing
from django.views.generic import DetailView
from .forms import ListingForm, RegisterForm, ListingEditForm
from django.urls import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.db.models import Q

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_detail.html'

def store(request):
    object_list = Listing.objects.all()
    query = request.GET.get("q")
    if query:
        object_list = object_list.filter(
            Q(listingname__icontains=query) | 
            Q(description__icontains=query)
        )
    object_list = object_list.filter(statuscompleted=False)
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
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

class ListingCreateView(CreateView):
    model = Listing
    fields = ['listingname', 'description', 'listingimage', 'price','currency']
    template_name = 'listing_form.html'
    success_url = reverse_lazy('store')

def login_view_custom(request):
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

def SearchListingView(request):
    query = request.GET.get('q')
    if query:
        results = Listing.objects.filter(listingname__icontains=query)
    else:
        results = []
    return render(request, 'store.html', {'results': results})

def MyListingView(request):
    object_list = Listing.objects.filter(listinguser=request.user)
    return render(request, 'my_listings.html', {'object_list': object_list})

@login_required
def password_change(request):
    if request.method == 'POST':
        current_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password1')
        confirm_password = request.POST.get('new_password2')
        if not request.user.check_password(current_password):
            return render(request, 'registration/password_change.html', {'error_message': 'Old password is incorrect'})
        if new_password != confirm_password:
            return render(request, 'registration/password_change.html', {'error_message': 'New password does not match'})
        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)
        return redirect('password_change_done')

    return render(request, 'registration/password_change.html')

def edit_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        form = ListingEditForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('store:my_listings')
    else:
        form = ListingEditForm(instance=listing)
    return render(request, 'edit_listing.html', {'form': form})
