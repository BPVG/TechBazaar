from django.views.generic import DetailView
from .models import Listing

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing_detail.html'