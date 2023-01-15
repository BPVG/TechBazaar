from django.shortcuts import render
from .models import Listing
from django.views.generic import DetailView

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_detail.html'

def store(request):
    object_list = Listing.objects.filter(statuscompleted = False)
    return render(request, 'alllistings.html', {'object_list': object_list})
