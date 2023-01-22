from django.shortcuts import render, redirect
from .models import Listing
from django.views.generic import DetailView
from .forms import ListingForm
from django.urls import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_detail.html'

def store(request):
    object_list = Listing.objects.filter(statuscompleted = False)
    return render(request, 'alllistings.html', {'object_list': object_list})

def create_listing(request):
    form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('store:store'))
    else:
        form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

class ListingCreateView(CreateView):
    model = Listing
    fields = ['listingname', 'description', 'listingimage', 'price','currency']
    template_name = 'listing_form.html'
    success_url = reverse_lazy('store')