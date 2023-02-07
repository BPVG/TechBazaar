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

class ListingCreateView(CreateView):
    model = Listing
    fields = ['listingname', 'description', 'listingimage', 'price','currency']
    template_name = 'listing_form.html'
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
