from django.shortcuts import render
from .models import Listing
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from .forms import ListingForm

def store(request):
    object_list = Listing.objects.filter(statuscompleted = False)
    return render(request, 'alllistings.html', {'object_list': object_list})

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_detail.html'

class ListingCreateView(CreateView):
    model = Listing
    template_name = 'create_listing.html'
    form_class = ListingForm
    success_url = reverse_lazy('store:store')