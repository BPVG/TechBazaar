from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ListingDetailView, ListingCreateView, MyListingView, edit_listing

app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('listing/<int:pk>/', ListingDetailView.as_view(), name='listing_detail'),
    path('listing/create/', ListingCreateView.as_view(), name='listing_create'),
    path('create/', views.create_listing, name='create_listing'),
    path('my_listings/', MyListingView, name='my_listings'),
    path('my_listings/edit/<int:pk>/', edit_listing, name='edit_listing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)