from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'listingname', 'listinguser']
    search_fields = ['listingname']

admin.site.register(Listing)